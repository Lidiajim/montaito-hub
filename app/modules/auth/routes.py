from flask import render_template, redirect, url_for, request, current_app
from itsdangerous import URLSafeTimedSerializer

from flask_login import current_user, login_user, logout_user

from app.modules.auth import auth_bp
from app.modules.auth.forms import SignupForm, LoginForm, RememberPassword, ResetPasswordForm
from app.modules.auth.services import AuthenticationService

from app import db


authentication_service = AuthenticationService()


@auth_bp.route("/signup/", methods=["GET", "POST"])
def show_signup_form():
    if current_user.is_authenticated:
        return redirect(url_for('public.index'))

    form = SignupForm()
    if form.validate_on_submit():
        email = form.email.data
        if not authentication_service.is_email_available(email):
            return render_template("auth/signup_form.html", form=form, error=f'Email {email} in use')

        try:
            user = authentication_service.create_with_profile(**form.data)
        except Exception as exc:
            return render_template("auth/signup_form.html", form=form, error=f'Error creating user: {exc}')

        # Log user
        login_user(user, remember=True)
        return redirect(url_for('public.index'))

    return render_template("auth/signup_form.html", form=form)


@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('public.index'))

    form = LoginForm()
    if request.method == 'POST' and form.validate_on_submit():
        if authentication_service.login(form.email.data, form.password.data):
            return redirect(url_for('public.index'))

        return render_template("auth/login_form.html", form=form, error='Invalid credentials')

    return render_template('auth/login_form.html', form=form)


@auth_bp.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('public.index'))


@auth_bp.route('/remember_my_password', methods=['GET', 'POST'])
def show_remember_my_password_form():
    if current_user.is_authenticated:
        return redirect(url_for('public.index'))

    form = RememberPassword()
    if request.method == 'POST' and form.validate_on_submit():
        if not authentication_service.is_email_available(form.email.data):
            user_mail = form.email.data
            token = authentication_service.generate_password_reset_token(user_mail)
            reset_url = url_for('auth.reset_password', token=token, _external=True)
            
            body = f"Usa el siguiente enlace para restablecer tu contraseña: {reset_url}"
            authentication_service.send_mail(
                "Restablecimiento de contraseña", body, "uvlhubpass@gmail.com", user_mail, "vvix cekw edup vaml"
            )
            return redirect(url_for('public.index'))

        return render_template("auth/remember_password_form.html", form=form, error='Invalid credentials')

    return render_template('auth/remember_password_form.html', form=form)


@auth_bp.route('/reset_password/<token>', methods=['GET', 'POST'])
def reset_password(token):
    email = authentication_service.verify_password_reset_token(token)
    if not email:
        return redirect(url_for('auth.show_remember_my_password_form', error='Token inválido o expirado'))

    form = ResetPasswordForm()
    if request.method == 'POST' and form.validate_on_submit():
        user = authentication_service.get_user_by_email(email)
        new_password = form.password.data
        user.set_password(new_password)
        
        db.session.commit()

        return redirect(url_for('public.index'))

    return render_template('auth/reset_password_form.html', form=form)



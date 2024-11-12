from flask import render_template, redirect, url_for, request
from flask_login import login_required, current_user
from app import db
from app.modules.profile import profile_bp
from app.modules.profile.forms import UserProfileForm, ResetPasswordForm
from app.modules.profile.services import UserProfileService
from app.modules.auth.services import AuthenticationService
from app.modules.dataset.models import DataSet

authentication_service = AuthenticationService()

@profile_bp.route("/profile/edit", methods=["GET", "POST"])
@login_required
def edit_profile():
    profile = authentication_service.get_authenticated_user_profile
    if not profile:
        return redirect(url_for("public.index"))

    form = UserProfileForm()
    if request.method == "POST":
        service = UserProfileService()
        result, errors = service.update_profile(profile.id, form)
        return service.handle_service_response(
            result, errors, "profile.edit_profile", "Profile updated successfully", "profile/edit.html", form
        )

    return render_template("profile/edit.html", form=form)


@profile_bp.route('/profile/summary')
@login_required
def my_profile():
    page = request.args.get('page', 1, type=int)
    per_page = 5

    user_datasets_pagination = db.session.query(DataSet) \
        .filter(DataSet.user_id == current_user.id) \
        .order_by(DataSet.created_at.desc()) \
        .paginate(page=page, per_page=per_page, error_out=False)

    total_datasets_count = db.session.query(DataSet) \
        .filter(DataSet.user_id == current_user.id) \
        .count()

    return render_template(
        'profile/summary.html',
        user_profile=current_user.profile,
        user=current_user,
        datasets=user_datasets_pagination.items,
        pagination=user_datasets_pagination,
        total_datasets=total_datasets_count
    )


@profile_bp.route('/profile/reset_password_link', methods=['POST'])
@login_required
def generate_password_reset_link():
    email = current_user.email
    token = authentication_service.generate_password_reset_token(email)
    reset_url = url_for('profile.reset_password', token=token, _external=True)
    return redirect(reset_url)


@profile_bp.route('/reset_password/<token>', methods=['GET', 'POST'])
def reset_password(token):
    email = authentication_service.verify_password_reset_token(token)
    if not email:
        return redirect(url_for('profile.my_profile', error='Token inválido o expirado'))

    form = ResetPasswordForm()
    if request.method == 'POST' and form.validate_on_submit():
        user = authentication_service.get_user_by_email(email)
        new_password = form.password.data
        user.set_password(new_password)
        db.session.commit()
        return redirect(url_for('profile.my_profile'))

    return render_template('profile/reset_password_form.html', form=form)
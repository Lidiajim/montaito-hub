from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Email, Length, EqualTo, Optional, Regexp

class UserProfileForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(max=100)])
    surname = StringField('Surname', validators=[DataRequired(), Length(max=100)])
    orcid = StringField('ORCID', validators=[
        Optional(),
        Length(min=19, max=19, message='ORCID must have 16 numbers separated by dashes'),
        Regexp(r'^\d{4}-\d{4}-\d{4}-\d{4}$', message='Invalid ORCID format')
    ])
    affiliation = StringField('Affiliation', validators=[
        Optional(),
        Length(min=5, max=100)
    ])
    submit = SubmitField('Save profile')

class ResetPasswordForm(FlaskForm):
    password = PasswordField('New Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[
        DataRequired(),
        EqualTo('password', message='Passwords must match')
    ])
    submit = SubmitField('Reset Password')
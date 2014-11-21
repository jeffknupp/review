from flask_wtf import Form
from wtforms import TextField, PasswordField
from wtforms.validators import DataRequired, ValidationError


class LoginForm(Form):
    email = TextField('Email address', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])


def passwords_match(form, field):
    if form.password.data != field.data:
        raise ValidationError("Passwords do not match")


class SignupForm(LoginForm):
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(),
                                                 passwords_match])

from flask_wtf import Form
from wtforms import TextField, PasswordField
from wtforms.validators import DataRequired

class LoginForm(Form):
    user_name = TextField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import InputRequired, Email, Length

class RegistrationForm(FlaskForm):
    
    username = StringField("username")
    password = PasswordField("password")
    confirm_password = PasswordField("confirm_password")
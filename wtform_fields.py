from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, EmailField, SubmitField
from wtforms.validators import InputRequired, Email, Length, EqualTo, ValidationError
from models import User

def user_exists(form, username):
    user_instance = User.query.filter_by(username=username.data).first()
    if user_instance:
        raise ValidationError("Username already exists. Please select a different username")
    
def email_exists(form, email):
    email_instance = User.query.filter_by(email=email.data).first()
    if email_instance:
        raise ValidationError("Email already in use. Please select a different username")

class SigninForm(FlaskForm):
    
    username = StringField("username", validators=[InputRequired(message="Please enter a username"), Length(min=4, max=15, message="Username must be between 4 and 15 characters"), user_exists])
    email = EmailField("email", validators=[InputRequired(message="Please enter your email address"), Email(message="Invalid email"), email_exists])
    password = PasswordField("password", validators=[InputRequired(message="Please enter a password"), Length(min=8, max=20, message="Password must be between 4 and 15 characters")])
    confirm_password = PasswordField("confirm_password", validators=[InputRequired(message="Please re-enter your password"), EqualTo('password', message="Passwords must match with the password above")])
    submit_button = SubmitField()

class LoginForm(FlaskForm):
    username = StringField("username", validators=[InputRequired(message="Please enter your username")])
    password = PasswordField("password", validators=[InputRequired(message="Please enter your password")])

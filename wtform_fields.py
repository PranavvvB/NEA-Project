from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, EmailField, SubmitField
from wtforms.validators import InputRequired, Email, Length, EqualTo, ValidationError
from models import User

def user_exists(form, username):
    """Checks if the username inputted by the user already exists in the database"""
    user_instance = User.query.filter_by(username=username.data).first()
    if user_instance:
        raise ValidationError("Username already exists. Please select a different username")
    
def email_exists(form, email):
    """Checks if the email inputted by the user already exists in the database"""
    email_instance = User.query.filter_by(email=email.data).first()
    if email_instance:
        raise ValidationError("Email already in use. Please select a different email")

def validate_credentials(form, field):
    """Validates the username and password inputted by the user"""
    username_inputted = form.username.data
    password_inputted = form.password.data

    # queries the database for the user inputted by the user
    user = User.query.filter_by(username=username_inputted).first()
    # checks if user exists in the database
    if user is None:
        raise ValidationError("Username or password is incorrect")
    
    # raises an error if the password inputted does not match the password in the database
    # effectively checks if the password is correct
    elif password_inputted != user.password:
        raise ValidationError("Username or password is incorrect")

class SigninForm(FlaskForm):
    # creates fields for the form to be filled out by the user and a submit button to submit the form
    username = StringField("username", validators=[InputRequired(message="Please enter a username"), Length(min=4, max=15, message="Username must be between 4 and 15 characters"), user_exists])
    email = EmailField("email", validators=[InputRequired(message="Please enter your email address"), Email(message="Invalid email"), email_exists])
    password = PasswordField("password", validators=[InputRequired(message="Please enter a password"), Length(min=8, max=20, message="Password must be between 4 and 15 characters")])
    confirm_password = PasswordField("confirm_password", validators=[InputRequired(message="Please re-enter your password"), EqualTo('password', message="Passwords must match with the password above")])
    submit_button = SubmitField("Sign Up")

class LoginForm(FlaskForm):
    # similar to the SigninForm class, but with different fields and validators
    username = StringField("username", validators=[InputRequired(message="Please enter your username")])
    password = PasswordField("password", validators=[InputRequired(message="Please enter your password"), validate_credentials])
    submit_button = SubmitField("Login")
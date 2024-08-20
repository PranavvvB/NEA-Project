from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, EmailField, SubmitField
from wtforms.validators import InputRequired, Email, Length, EqualTo

class SigninForm(FlaskForm):
    
    username = StringField("username", validators=[InputRequired(message="Please enter a username"), Length(min=4, max=15, message="Username must be between 4 and 15 characters")])
    email = EmailField("email", validators=[InputRequired(message="Please enter your email address"), Email(message="Invalid email")])
    password = PasswordField("password", validators=[InputRequired(message="Please enter a password"), Length(min=4, max=15, message="Password must be between 4 and 15 characters")])
    confirm_password = PasswordField("confirm_password", validators=[InputRequired(message="Please re-enter your password"), EqualTo('password', message="Passwords must match with the password above")])
    submit_button = SubmitField()

class LoginForm(FlaskForm):
    username = StringField("username", validators=[InputRequired(message="Please enter your username")])
    password = PasswordField("password", validators=[InputRequired(message="Please enter your password")])

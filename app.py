import os
from flask import Flask, url_for, redirect, request, session, render_template, flash

from wtform_fields import *
from models import db

app = Flask(__name__)  
app.secret_key = "REPLACE KEY LATER"

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{os.path.join(basedir, "data.db")}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False  # prevents "significant amount of overhead to every session"

db.init_app(app)

with app.app_context():
    db.create_all()

@app.route("/")
def index():

    return render_template("index.html")

@app.route("/signup", methods=["GET","POST"])
def signin():

    signup_form = SigninForm()

    if signup_form.validate_on_submit():
        username = signup_form.username.data
        password = signup_form.password.data
        email = signup_form.email.data

        user = User(username=username, email=email, password=password)
        db.session.add(user)
        db.session.commit()

        return redirect(url_for("login"))
    

    return render_template("signup.html", form=signup_form)

@app.route("/login", methods=["GET","POST"])
def login():
    login_form = LoginForm()

    if login_form.validate_on_submit():
        return redirect(url_for("chat"))
    return render_template("login.html", form=login_form)

@app.route("/chat", methods=["GET","POST"])
def chat():

    return render_template("chat.html")
   
if __name__ == "__main__":
    app.run(debug=True)
# app local browser link : http://127.0.0.1:5000/
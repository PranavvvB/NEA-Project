from flask import Flask, url_for, redirect, request, session, render_template, flash
from wtform_fields import *

app = Flask(__name__)
app.secret_key = "REPLACE KEY LATER"

# @app.route('/', methods=["GET"])
# def index():

#     return render_template("index.html")

@app.route('/', methods=["GET",'POST'])
def signin():

    signup_form = SigninForm()

    if signup_form.validate_on_submit():
        return redirect(url_for("chat"))
    

    return render_template("signup.html", form=signup_form)

@app.route("/login", methods=["GET",'POST'])
def login():
    login_form = LoginForm()

    if login_form.validate_on_submit():
        return redirect(url_for("chat"))

@app.route("/chat", methods=["GET","POST"])
def chat():

    return render_template("chat.html")
   
if __name__ == "__main__":
    app.run(debug=True)
# app local browser link : http://127.0.0.1:5000/
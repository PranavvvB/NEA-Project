import os
from flask import Flask, url_for, redirect, render_template, flash
from flask_login import LoginManager, login_user, login_required, logout_user
from flask_migrate import Migrate


from wtform_fields import *
from models import *

# initialise flask app
app = Flask(__name__)  
app.secret_key = "REPLACE KEY LATER"

# setting path to database
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{os.path.join(basedir, "data.db")}'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False  # prevents "significant amount of overhead to every session"


migrate = Migrate(app, db)

# initialise database
db.init_app(app)

# configure flask login
login = LoginManager(app)
login.init_app(app)

@login.user_loader
def load_user(id):
    return db.session.get(User, int(id))

@app.route("/")
def index():

    return render_template("index.html")

@app.route("/signup", methods=["GET","POST"])
def signup():

    signup_form = SignupForm()

    if signup_form.validate_on_submit():
        username = signup_form.username.data
        password = signup_form.password.data
        email = signup_form.email.data

        # Hashes email and password
        hashed_password = pbkdf2_sha256.hash(password)

        # Adds user to database
        user = User(username=username, email=email, password=hashed_password)
        db.session.add(user)
        db.session.commit()

        flash("Registered successfully. Please login.", "success")
        return redirect(url_for("login"))
    
    return render_template("signup.html", form=signup_form)

@app.route("/login", methods=["GET","POST"])
def login():
    login_form = LoginForm()

    # validates the form when the user submits it
    if login_form.validate_on_submit():
        user_object = User.query.filter_by(username=login_form.username.data).first()
        login_user(user_object) # logs in the user

        flash("Logged in successfully", "success")
        return redirect(url_for("chat"))
    
    return render_template("login.html", form=login_form)

@app.route("/chat", methods=["GET","POST"])
@login_required
def chat():

    return render_template("chat.html")

@app.route("/logout", methods=["GET"])
def logout():
    logout_user()

    flash("Logged out successfully", "success")
    return redirect(url_for("login"))
   
if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)

# app local browser link : http://127.0.0.1:5000/
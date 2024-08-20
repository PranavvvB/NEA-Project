import os
from flask import Flask
from models import *
from app import app, db

app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))

app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{os.path.join(basedir, "data.db")}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False  # prevents "significant amount of overhead to every session"

db.init_app(app)

if __name__ == "__main__":
    with app.app_context():
        db.create_all()



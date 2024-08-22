from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(UserMixin, db.Model):
    """Creates a table in the database to store user information"""
    __tablename__ = "users"  # to access the table, we use this name
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(15), unique=True, nullable=False)
    email = db.Column(db.String(), nullable=False)
    password = db.Column(db.String(20), nullable=False)

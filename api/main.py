import sqlite3
from datetime import datetime

from flask import Flask
from flask_sqlalchemy import SQLAlchemy


APP = Flask(__name__)

APP.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
APP.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///db_form.sqlite3"

DB = SQLAlchemy(APP)


class User(DB.Model):
    """Model for user accounts"""

    __tablename__ = 'users'
    id = DB.Column(DB.Integer, primary_key=True)
    name = DB.Column(DB.String(120), nullable=False)
    region = DB.Column(DB.String(50))
    email = DB.Column(DB.String(50), unique=True, nullable=False)
    date_created = DB.Column(DB.DateTime, default=datetime.now)


@APP.route('/')
@APP.route('/index')
def hello_world():
    return 'Hello World!'


def main():
    DB.create_all()
    APP.run(host='0.0.0.0', debug=True)


if __name__ == "__main__":
    main()

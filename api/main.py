import sqlite3
from datetime import datetime

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import exc


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


@APP.route('/users', methods=['GET'])
def view_users():
    users = User.query.order_by(User.name).all()
    users_list = []
    for user in users:
        info = {
            'name': user.name,
            'email': user.email,
            'region': user.region,
        }
        users_list.append(info)
    return jsonify(users_list)


@APP.route('/register', methods=['GET'])
def register_user():
    try:
        name = request.args.get('name')
        region = request.args.get('region')
        email = request.args.get('email')
        new_user = User(name=name, region=region, email=email)
        DB.session.add(new_user)
        DB.session.commit()
        return (success_response('Registered user!'), 200)
    except exc.IntegrityError:
        missing_args = []
        if name is None:
            missing_args.append('name')
        if region is None:
            missing_args.append('region')
        if email is None:
            missing_args.append('email')
        DB.session.rollback()
        return (error_response(missing_args), 400)

@APP.route('/')
@APP.route('/index')
def hello_world():
    return 'Hello World!'


def success_response(message):
    return json_response(200, 'OK', message)

def error_response(args_list):
    msg_list = []
    message = ''
    for arg in args_list:
        message = f'Missing parameter {arg}'
        msg_list.append(message)
    return json_response(400, 'Bad request', msg_list)


def json_response(code, status, message):
    return {
        'Status': code,
        'StatusText': status,
        'Message': message,
    }


def main():
    DB.create_all()
    APP.run(host='0.0.0.0', debug=True)


if __name__ == "__main__":
    main()

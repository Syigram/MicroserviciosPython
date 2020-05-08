from flask import request, make_response, jsonify
from flask import current_app as app
from sqlalchemy import exc

from app.extensions import db
from models.user import User
from .utilities import error_response, success_response, json_response


@app.route('/')
@app.route('/index')
def hello_world():
    return 'Hello World!'


@app.route('/users', methods=['GET'])
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


@app.route('/register', methods=['GET'])
def register_user():
    try:
        name = request.args.get('name')
        region = request.args.get('region')
        email = request.args.get('email')
        new_user = User(name=name, region=region, email=email)
        db.session.add(new_user)
        db.session.commit()
        return (success_response('Registered user!'), 200)
    except exc.IntegrityError:
        missing_args = []
        if name is None:
            missing_args.append('name')
        if region is None:
            missing_args.append('region')
        if email is None:
            missing_args.append('email')
        db.session.rollback()
        return (error_response(missing_args), 400)

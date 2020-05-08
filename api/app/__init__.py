from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from models.user import User
from config.config import Config
from .extensions import db


def create_app():
    app = Flask(__name__)
    app.debug = True

    app.config.from_object(Config)

    db.init_app(app)

    with app.app_context():
        from . import routes  # Import routes
        db.create_all()  # Create database tables for our data models

        return app

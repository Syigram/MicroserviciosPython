from datetime import datetime

from app.extensions import db

class User(db.Model):
    """Model for user accounts"""

    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    region = db.Column(db.String(50))
    email = db.Column(db.String(50), unique=True, nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.now)

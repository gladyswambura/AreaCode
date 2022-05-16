from datetime import datetime
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from app import db
from . import login_manager


class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), nullable=False, unique=True)
    email = db.Column(db.String(255), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False,  unique=True)
    comment = db.relationship('Comment', backref='username', lazy='dynamic')

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    def set_password(self, password):
        pass_hash = generate_password_hash(password)
        self.password = pass_hash

    def verify_password(self, password):
        return check_password_hash(self.password, password)

    def __repr__(self):
        return f'User: {self.username}'


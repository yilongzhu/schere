from flask import current_app
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(128), index=True, unique=True)
    password = db.Column(db.String(128))
    shares = db.relationship('Share', backref='user')

    def __repr__(self):
        return  '<User \'{}\'>'.format(self.email)

    def set_password(self, password):
        self.password = generate_password_hash(password)
    
    def check_password(self, password):
        return check_password_hash(self.password, password)


class Share(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(140), nullable=False)
    timestamp = db.Column(db.DateTime, nullable=False, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return  '<Share \'{}\'>'.format(self.body)

    def update(self, new_body):
        self.body = new_body
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
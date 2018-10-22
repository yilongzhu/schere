from flask import current_app
from datetime import datetime
from app import db


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(140), nullable=False)
    timestamp = db.Column(db.DateTime, nullable=False, index=True, default=datetime.utcnow)

    def __repr__(self):
        return  '<Post \'{}\'>'.format(self.body)

    def delete(self):
        db.session.delete(self)
        db.session.commit()
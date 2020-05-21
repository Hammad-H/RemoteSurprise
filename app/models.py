from datetime import datetime

from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(64), index = True, unique = True)
    email = db.Column(db.String(120), index = True, unique = True)
    password_hash = db.Column(db.String(128))
    recommendations = db.relationship('Recommendation', backref='author', lazy='dynamic')

    def __repr__(self):
        return '<User {}'.format(self.username)


class Recommendation(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(140))
    type = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime, index = True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    friend_name = db.Column(db.String(140))

    def __repr__(self):
        return '<Recommdation {}'.format(self.title)

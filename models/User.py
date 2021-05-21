from enum import unique
from .db import db

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, unique=True)
    location = db.Column(db.String, nullable=False)
    about_me = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)
    def to_json(self):
        return {
        "id": self.id,
        "name": self.name,
        "location": self.location,
        "about_me": self.about_me,
        "email": self.email,
        }
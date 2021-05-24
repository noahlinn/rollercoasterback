from .db import db

class Roller_Coaster(db.Model):
    __tablename__ = 'roller_coasters'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    park_located_at = db.Column(db.String, nullable=False)
    location = db.Column(db.String, nullable=False)
    type_of = db.Column(db.String, nullable=False)
    length_in_feet = db.Column(db.Integer, nullable=False)
    height_in_feet = db.Column(db.Integer, nullable=False)
    number_of_inversions = db.Column(db.Integer)
    manufacturer = db.Column(db.String)
    video = db.Column(db.String)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
from .db import db

class Roller_Coaster(db.Model):
    __tablename__ = 'roller_coasters'
    id = db.Column(db.Integer, primary_key=True)
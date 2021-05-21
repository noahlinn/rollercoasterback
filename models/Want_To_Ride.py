from .db import db

class Want_To_Ride(db.Model):
    __tablename__ = 'want_to_rides'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    coaster_id = db.Column(db.Integer, db.ForeignKey('roller_coasters.id'))
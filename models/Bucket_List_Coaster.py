from .db import db

class Bucket_List_Coaster(db.Model):
    __tablename__ = 'bucket_list_coasters'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    coaster_id = db.Column(db.Integer, db.ForeignKey('roller_coasters.id'))
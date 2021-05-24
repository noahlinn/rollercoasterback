from .db import db

class Roller_Coaster(db.Model):
    __tablename__ = 'roller_coasters'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    park_located_at = db.Column(db.String, nullable=False)
    location = db.Column(db.String, nullable=False)
    year_built = db.Column(db.Integer)
    type_of = db.Column(db.String, nullable=False)
    top_speed_in_mph = db.Column(db.Integer, nullable=False)
    length_in_feet = db.Column(db.Integer, nullable=False)
    height_in_feet = db.Column(db.Integer, nullable=False)
    number_of_inversions = db.Column(db.Integer)
    manufacturer = db.Column(db.String)
    image = db.Column(db.String)
    video = db.Column(db.String)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    def to_json(self):
        return {
        "id": self.id,
        "name": self.name,
        "location": self.location,
        "park_located_at": self.park_located_at,
        "type_of": self.type_of,
        "top_speed_in_mph": self.top_speed_in_mph,
        "length_in_feet": self.length_in_feet,
        "height_in_feet": self.height_in_feet,
        "length_in_feet": self.length_in_feet,
        "number_of_inversions": self.number_of_inversions,
        "manufacturer": self.manufacturer,
        "image": self.image,
        "video": self.video,
        "user_id": self.user_id
        }
from flask import request, Flask
import models

def create_coaster():
    coaster = models.Roller_Coaster(
        name = request.json["name"],
        park_located_at = request.json["park_located_at"],
        location = request.json["location"],
        type_of = request.json["type_of"],
        length_in_feet = request.json["length_in_feet"],
        height_in_feet = request.json["height_in_feet"],
        number_of_inversions = request.json["number_of_inversions"],
        manufacturer = request.json["manufacturer"],
        video = request.json["video"],
        user_id = request.headers["Authorization"]
    )
    models.db.session.add(coaster)
    models.db.session.commit()
    return "OK"

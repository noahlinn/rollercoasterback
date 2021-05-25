from flask import request, Flask
from flask_sqlalchemy.model import Model
import models

def create_coaster():
    print(request.json)
    coaster = models.Roller_Coaster(
        name = request.json["name"],
        park_located_at = request.json["park_located_at"],
        location = request.json["location"],
        year_built = request.json["year_built"],
        type_of = request.json["type_of"],
        top_speed_in_mph = request.json["top_speed_in_mph"],
        length_in_feet = request.json["length_in_feet"],
        height_in_feet = request.json["height_in_feet"],
        number_of_inversions = request.json["number_of_inversions"],
        manufacturer = request.json["manufacturer"],
        image = request.json["image"],
        video = request.json["video"],
        user_id = request.headers["Authorization"]
    )
    models.db.session.add(coaster)
    models.db.session.commit()
    return {"new_coaster": coaster.to_json()}

def search_coasters_by_name():
    query = request.json["query"]
    print(query)
    coaster = models.Roller_Coaster.query.filter(models.Roller_Coaster.name.ilike(f'%{query}%')).all()
    if not coaster:
        return{"message": "No Roller Coasters Found"}, 404
    return {"results": [c.to_json() for c in coaster]}

def seeding():
    coaster1 = models.Roller_Coaster(
        name = "Batman The Ride",
        park_located_at = "Six Flags Over Georgia",
        location = "Austell, Georgia, United States",
        year_built = 1997,
        type_of = "Inverted Coaster",
        top_speed_in_mph = 50,
        length_in_feet = 2700,
        height_in_feet = 105,
        number_of_inversions = 5,
        manufacturer = "Bolliger & Mabillard",
        image = "https://sf-static.sixflags.com/wp-content/uploads/2020/04/batman4-3-scaled.jpg",
        video = "WBpYXaLppE4"
    )
    coaster2 = models.Roller_Coaster(
        name = "Blue Hawk",
        park_located_at = "Six Flags Over Georgia",
        location = "Austell, Georgia, United States",
        year_built = 1992,
        type_of = "Steel Looping",
        top_speed_in_mph = 52,
        length_in_feet = 2739,
        height_in_feet = 122,
        number_of_inversions = 5,
        manufacturer = "Vekoma",
        image = "https://sf-static.sixflags.com/wp-content/uploads/2020/04/img_0226_0-2-scaled.jpg",
        video = "NKfNGhLDKfo"
    )
    coaster3 = models.Roller_Coaster(
        name = "Dahlonega Mine Train",
        park_located_at = "Six Flags Over Georgia",
        location = "Austell, Georgia, United States",
        year_built = 1967,
        type_of = "Mine Train",
        top_speed_in_mph = 29,
        length_in_feet = 2327,
        height_in_feet = 37,
        number_of_inversions = 0,
        manufacturer = "Vekoma",
        image = "https://static.wikia.nocookie.net/sixflags/images/1/19/DahlonegaMineTrain.jpg",
        video = "3VSMEWlkb6k"
    )
    coaster4 = models.Roller_Coaster(
        name = "Dare Devil Dive",
        park_located_at = "Six Flags Over Georgia",
        location = "Austell, Georgia, United States",
        year_built = 2011,
        type_of = "Euro-Fighter",
        top_speed_in_mph = 52,
        length_in_feet = 2099,
        height_in_feet = 95,
        number_of_inversions = 3,
        manufacturer = "Gerstlauer",
        image = "https://live.staticflickr.com/65535/40823559863_eff3c9556b_k.jpg",
        video = "vQ2awFmEfG0"
    )
    coaster5 = models.Roller_Coaster(
        name = "Georgia Scorcher",
        park_located_at = "Six Flags Over Georgia",
        location = "Austell, Georgia, United States",
        year_built = 1999,
        type_of = "Stand-Up Coaster",
        top_speed_in_mph = 54,
        length_in_feet = 3000,
        height_in_feet = 101,
        number_of_inversions = 2,
        manufacturer = "Bolliger & Mabillard",
        image = "https://1.bp.blogspot.com/-BvQJFXWUbMQ/XvlB_V3L6VI/AAAAAAAA5qk/Xlo-FBjAu3Y9NHJ0KxfK4bhFznkDg6UmgCLcBGAsYHQ/s1600/2.JPG",
        video = "1Bwu0C2Qbxg"
    )
    coaster6 = models.Roller_Coaster(
        name = "Goliath",
        park_located_at = "Six Flags Over Georgia",
        location = "Austell, Georgia, United States",
        year_built = 2006,
        type_of = "Hyper Coaster",
        top_speed_in_mph = 70,
        length_in_feet = 4480,
        height_in_feet = 200,
        number_of_inversions = 0,
        manufacturer = "Bolliger & Mabillard",
        image = "http://www.negative-g.com/six-flags-over-georgia/2011/SFOG-5-29-2011-Goliath-5.jpg",
        video = "A_K-IjnkMIg"
    )
    coaster7 = models.Roller_Coaster(
        name = "Great American Scream Machine",
        park_located_at = "Six Flags Over Georgia",
        location = "Austell, Georgia, United States",
        year_built = 1973,
        type_of = "Wood Coaster",
        top_speed_in_mph = 57,
        length_in_feet = 3450,
        height_in_feet = 105,
        number_of_inversions = 0,
        manufacturer = "Philadelphia Toboggan Coasters",
        image = "https://sf-static.sixflags.com/wp-content/uploads/2020/04/sfog_great_american_scream_machine_1440x1533-3.jpg",
        video = "LvNvXpFq4do"
    )
    coaster8 = models.Roller_Coaster(
        name = "Joker Funhouse Coaster",
        park_located_at = "Six Flags Over Georgia",
        location = "Austell, Georgia, United States",
        year_built = 2004,
        type_of = "Big Dipper",
        top_speed_in_mph = 30,
        length_in_feet = 900,
        height_in_feet = 28,
        number_of_inversions = 0,
        manufacturer = "Chance Rides",
        image = "https://upload.wikimedia.org/wikipedia/commons/3/39/Wile_E._Coyote_Canyon_Blaster_%28Six_Flags_Over_Georgia%29_02.jpg",
        video = "dXUMn81cq-E"
    )
    coaster9 = models.Roller_Coaster(
        name = "Superman - Ultimate Flight",
        park_located_at = "Six Flags Over Georgia",
        location = "Austell, Georgia, United States",
        year_built = 2002,
        type_of = "Flying Coaster",
        top_speed_in_mph = 51,
        length_in_feet = 2759,
        height_in_feet = 106,
        number_of_inversions = 2,
        manufacturer = "Bolliger & Mabillard",
        image = "https://www.tripsavvy.com/thmb/NCVQKIysE3afXcvF36G96TenIyw=/811x0/filters:no_upscale():max_bytes(150000):strip_icc():format(webp)/supermanultimateflightnew-5c2c394cc9e77c0001269673.jpg",
        video = "7RxCgEJP4Y"
    )
    coaster10 = models.Roller_Coaster(
        name = "Twisted Cyclone",
        park_located_at = "Six Flags Over Georgia",
        location = "Austell, Georgia, United States",
        year_built = 2018,
        type_of = "IBox Hybrid Coaster",
        top_speed_in_mph = 50,
        length_in_feet = 2400,
        height_in_feet = 100,
        number_of_inversions = 3,
        manufacturer = "Rocky Mountain Construction",
        image = "https://www.coaster101.com/wp-content/uploads/2018/05/IMG_2987.jpg",
        video = "Baa-x29rT30"
    )
    # coaster_list = []
    # for n in range (1, 10+1):
    #     string_n = str(n)
    #     coaster = f'coaster{string_n}'
    #     coaster_list.append(coaster)
    # print(coaster_list)
    models.db.session.add_all([coaster7, coaster6, coaster5, coaster4, coaster3, coaster2, coaster1])
    models.db.session.commit()
    return "seeded"

def get_one_coaster(id):
    coaster = models.Roller_Coaster.query.filter_by(id = id).first()
    if not coaster:
        return{"message": "No Roller Coaster"}, 404
    if request.method == "GET":
        return{"roller_coaster": coaster.to_json()}
    elif request.method == "PUT":
        coaster.name = request.json["name"],
        coaster.park_located_at = request.json["park_located_at"],
        coaster.location = request.json["location"],
        coaster.year_built = request.json["year_built"],
        coaster.type_of = request.json["type_of"],
        coaster.top_speed_in_mph = request.json["top_speed_in_mph"],
        coaster.length_in_feet = request.json["length_in_feet"],
        coaster.height_in_feet = request.json["height_in_feet"],
        coaster.number_of_inversions = request.json["number_of_inversions"],
        coaster.manufacturer = request.json["manufacturer"],
        coaster.image = request.json["image"],
        coaster.video = request.json["video"]
        models.db.session.add(coaster)
        models.db.session.commit()
        return{"roller_coaster": coaster.to_json()}
    

    
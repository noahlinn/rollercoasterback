import re
from flask import request, Flask
from sqlalchemy.orm import query
import models
import jwt
from flask_bcrypt import Bcrypt
import os
app = Flask(__name__)
bcrypt = Bcrypt(app)

def create_user():
    existing_user = models.User.query.filter_by(email = request.json["email"]).first()
    if existing_user:
        return{"message": "Email must be unique"}, 400
    hashed_pw = bcrypt.generate_password_hash(request.json["password"]).decode('utf-8')
    user = models.User(
        name = request.json["name"],
        email = request.json["email"],
        location = request.json["location"],
        about_me = request.json["about_me"],
        password = hashed_pw
    )
    models.db.session.add(user)
    models.db.session.commit()
    encrypted_id = jwt.encode({ "user_id": user.id }, os.environ.get('JWT_SECRET'), algorithm="HS256")

    return{"user": user.to_json(), "user_id": encrypted_id}

def login():
    user = models.User.query.filter_by(email=request.json["email"]).first()
    if not user:
        return{"message": "User not found"}, 404
    if bcrypt.check_password_hash(user.password, request.json["password"]):
        encrypted_id = jwt.encode({"user_id": user.id}, os.environ.get('JWT_SECRET'), algorithm = "HS256")
        return {"user": user.to_json(), "user_id": encrypted_id}
    else:
        return{"message": "Password incorrect"}, 401

def verify():
    decrypted_id = jwt.decode(request.headers["Authorization"], os.environ.get('JWT_SECRET'), algorithms=["HS256"])["user_id"]
    user = models.User.query.filter_by(id=decrypted_id).first()
    if not user:
        return{"message": "user not found"},404
    return{"user": user.to_json()}

def one_user(id):
    user = models.User.query.filter_by(id = id).first()
    if not user:
        return{"message": "user not found"},404
    return{"user": user.to_json()}

def credits(id):
    if request.method == "PUT" or request.method == "DELETE":
        decrypted_id = jwt.decode(request.headers["Authorization"], os.environ.get('JWT_SECRET'), algorithms=["HS256"])["user_id"]
        user = models.User.query.filter_by(id=decrypted_id).first()
        if not user:
            return{"message": "User Not Found"}, 404
        coaster = models.Roller_Coaster.query.filter_by(id = id).first()
        if not coaster:
            return{"message": "No Roller Coaster"}, 404
        if request.method == "PUT":
            user.credits.append(coaster)
        elif request.method == "DELETE":
            user.credits.remove(coaster)
        models.db.session.add_all([user, coaster])
        models.db.session.commit()
        return{"Message": "Associated or Dissociated"}
    elif request.method == "GET":
        user = models.User.query.filter_by(id = id).first()
        if not user:
            return{"message": "User Not Found"}, 404
        coasters = user.credits
        if not coasters:
            return{"message": "No Coasters Found"}, 404
        return {"credits" : [c.to_json() for c in coasters]}


def add_to_bucketlist(id):
    if request.method == "PUT" or request.method == "DELETE":
        decrypted_id = jwt.decode(request.headers["Authorization"], os.environ.get('JWT_SECRET'), algorithms=["HS256"])["user_id"]
        user = models.User.query.filter_by(id=decrypted_id).first()
        if not user:
            return{"message": "User Not Found"}, 404
        coaster = models.Roller_Coaster.query.filter_by(id = id).first()
        if not coaster:
            return{"message": "No Roller Coaster"}, 404
        if request.method == "PUT":
            user.bucketlists.append(coaster)
        elif request.method == "DELETE":
            user.bucketlists.remove(coaster)
        models.db.session.add_all([user, coaster])
        models.db.session.commit()
        return {"message": "Added or Removed from bucket list"}
    elif request.method == "GET":
        user = models.User.query.filter_by(id = id).first()
        if not user:
            return{"message": "User Not Found"}, 404
        coasters = user.bucketlists
        if not coasters:
            return{"message": "No Coasters Found"}, 404
        return {"bucket_list" : [c.to_json() for c in coasters]}

def search_by_name():
    query = request.json["query"]
    user = models.User.query.filter(models.User.name.ilike(f'%{query}%')).all()
    if not user:
        return{"message": "No Users Found"}, 404
    return {"results": [u.to_json() for u in user]}
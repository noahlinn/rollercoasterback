import re
from flask import request, Flask, jsonify
from sqlalchemy.orm import query
import models
import jwt
from flask_bcrypt import Bcrypt
import os
import cloudinary as cloudinary, cloudinary.uploader
app = Flask(__name__)
bcrypt = Bcrypt(app)

cloudinary.config(cloud_name = os.environ.get('CLOUD_NAME'), api_key=os.environ.get('API_KEY'), 
    api_secret=os.environ.get('API_SECRET'))

def create_user():
    file_to_upload = request.files["file"]
    
    upload_result = cloudinary.uploader.upload(file_to_upload)

    existing_user = models.User.query.filter_by(email = request.form["email"]).first()
    if existing_user:
        return{"message": "Email must be unique"}, 400
    hashed_pw = bcrypt.generate_password_hash(request.form["password"]).decode('utf-8')

    user = models.User(
        name = request.form["name"],
        email = request.form["email"],
        location = request.form["location"],
        about_me = request.form["about_me"],
        password = hashed_pw,
        profile_pic = upload_result["url"]
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

def search_by_location():
    query = request.json["query"]
    user = models.User.query.filter(models.User.location.ilike(f'%{query}%')).all()
    if not user:
        return{"message": "No Users Found"}, 404
    return {"results": [u.to_json() for u in user]}
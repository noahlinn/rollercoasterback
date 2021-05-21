from flask import request, Flask
import models
import jwt
from flask_bcrypt import Bcrypt
import os
app = Flask(__name__)
bcrypt = Bcrypt(app)
def create_user():
    existing_user = models.User.query.filter_by(email = request.json["email"]).first()
    if existing_user:
        return{"message": "Email must be presenet and unique"}, 400
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

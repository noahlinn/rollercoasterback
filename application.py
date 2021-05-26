import os 
from dotenv  import load_dotenv
from flask import Flask, request
import sqlalchemy
from flask_cors import CORS

import models
from routes import apply_routes 

load_dotenv()
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"]= os.environ.get('DATABASE_URL').replace('postgress', 
'postgresql')
models.db.init_app(app)
CORS(app)
def root():
  return { "message": "ok" }
app.route('/', methods=["GET"])(root)

apply_routes(app)

if __name__ == '__main__':
  port = int(os.environ.get('PORT', 5000))
  app.run(host='0.0.0.0', port=port, debug=True)
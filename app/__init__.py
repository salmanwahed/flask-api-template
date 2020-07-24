from flask import Flask
from flask_marshmallow import Marshmallow
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy(app=app)
ma = Marshmallow(app)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///contact.db"

api = Api(app)

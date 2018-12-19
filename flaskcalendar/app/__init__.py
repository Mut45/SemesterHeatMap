from flask import Flask
from flask import request, render_template, jsonify
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import json



app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import routes,models

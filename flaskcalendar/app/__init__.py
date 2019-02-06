from flask import Flask
from flask import request, render_template, jsonify
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import json




app = Flask(__name__)
app.config.from_object(Config)
app.secret_key = b'?d??R???kq@XJD=?'
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import routes,models

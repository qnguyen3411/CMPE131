from flask import Flask

from app import config
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)
app.config.from_object(config.Config)

db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)

from app import routes
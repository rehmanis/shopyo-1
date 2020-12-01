"""
All initialisations like db = SQLAlchemy in this file
"""

from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_login import LoginManager
from flask_migrate import Migrate

from flask_uploads import IMAGES, UploadSet

db = SQLAlchemy()
ma = Marshmallow()
login_manager = LoginManager()
migrate = Migrate()

productphotos = UploadSet("productphotos", IMAGES)
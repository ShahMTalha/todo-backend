import os

from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
schema = os.environ.get('CURRENT_SCHEMA')

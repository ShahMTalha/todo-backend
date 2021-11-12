from flask import Flask
from src.config import app_config
from flask_cors import CORS

from src.models import db
from src import api_todo as todo_blueprint


def create_app(app_env):
    app = Flask(__name__)
    CORS(app, support_credentials=True)
    cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
    app.config['JSON_SORT_KEYS'] = False
    app.config.from_object(app_config[app_env])
    db.init_app(app)

    app.register_blueprint(todo_blueprint, url_prefix='/todo')

    @app.route('/')
    def index():
        return "Welcome to Flask API"

    return app
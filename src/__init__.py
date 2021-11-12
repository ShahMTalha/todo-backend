from flask import Flask, Blueprint

app = Flask(__name__)

api_todo = Blueprint('todo', __name__)

from . import controllers


# @api_oc.before_request
# def before_request_function():
#     return True


@api_todo.route('/')
def index():
    return "I am at todo start"
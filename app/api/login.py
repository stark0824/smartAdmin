from flask import Blueprint

login = Blueprint('login', __name__)


@login.route('/login')
def loginIndex():
    return "login Hello"

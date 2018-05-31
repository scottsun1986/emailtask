from flask import Blueprint

auth=Blueprint('auth',__name__)


from . import views


@auth.route('/')
@auth.route('/index')
def index():
    return "Hello, World!"
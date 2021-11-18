from flask import Blueprint

auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    return "login"

@auth.route('/logout')
def logout():
    return "login"

@auth.route('/sign-up')
def signup():
    return "login"
from flask import Blueprint

bp = Blueprint('main', __name__)

@bp.route('/')
def home():
    return "<h1>🎉 IT'S WORKING! 🎉</h1><p>Your Flask app is alive, my love!</p>"

@bp.route('/hello')
def hello():
    return "<h1>Hello! ❤️</h1>"
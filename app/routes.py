from flask import Blueprint, render_template
from flask_login import login_required, current_user

bp = Blueprint('main', __name__)

@bp.route('/')
def home():
    return render_template('base.html', title='Home')

@bp.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html', user=current_user)

@bp.route('/hello')
def hello():
    return "<h1>Flask application is running.</h1>"
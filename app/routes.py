print("routes.py is being loaded!")

from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from . import db
from .models import Book
from .auth import admin_required

bp = Blueprint('main', __name__)


@bp.route('/')
def home():
    return render_template('base.html', title='Home')

@bp.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html', user=current_user)

@bp.route('/books/add', methods=['GET', 'POST'])
@login_required
@admin_required
def add_book():
    if request.method == 'POST':
        title = request.form.get('title')
        author = request.form.get('author')
        category = request.form.get('category')
        price = float(request.form.get('price'))
        language = request.form.get('language')
        stock = int(request.form.get('stock'))
        
        new_book = Book(
            title=title,
            author=author,
            category=category,
            price=price,
            language=language,
            stock=stock
        )
        
        db.session.add(new_book)
        db.session.commit()
        
        flash('Book added successfully.')
        return redirect(url_for('main.add_book'))
    
    return render_template('add_book.html')
@bp.route('/test')
def test():
    return "Test route is working!"

@bp.route('/hello')
def hello():
    return "<h1>Flask application is running.</h1>"
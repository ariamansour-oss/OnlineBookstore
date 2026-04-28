from app import create_app, db
from app.models import Book

app = create_app()

with app.app_context():
    books = Book.query.all()
    print("Books in database:")
    for b in books:
        print(f"ID: {b.id}, Title: {b.title}, Author: {b.author}, Price: ${b.price}, Stock: {b.stock}")
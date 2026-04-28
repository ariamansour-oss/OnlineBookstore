from app import create_app, db
from app.models import User

app = create_app()

with app.app_context():
    users = User.query.all()
    print("All users in database:")
    for u in users:
        print(f"Email: {u.email}, Role: {u.role}")
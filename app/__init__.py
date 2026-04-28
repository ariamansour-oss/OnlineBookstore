from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)
    
    app.config['SECRET_KEY'] = 'your-secret-key-change-this-in-production'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///bookstore.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'
    
    # Import models here to avoid circular import
    from .models import User
    
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))
    
    # Import and register blueprints
    from .routes import bp
    app.register_blueprint(bp)
    
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)
    
    with app.app_context():
        db.create_all()
    
    return app
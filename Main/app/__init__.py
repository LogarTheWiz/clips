from flask import Flask
from flask_mail import Mail
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
import os


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'your-secret-key'

    # Register Blueprints
    from .routes import routes
    from .errors import errors, error_handlers
    app.register_blueprint(routes)
    app.register_blueprint(account)
    app.register_blueprint(errors)
    error_handlers(app)
    
    # Initialize extensions
    db.init_app(app)
    bcrypt.init_app(app)
    mail.init_app(app)
    login_manager.init_app(app)

    return app
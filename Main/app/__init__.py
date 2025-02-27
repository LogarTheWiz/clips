from flask import Flask
import os

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'your-secret-key'

    from .routes import routes
    from .errors import errors, error_handlers
    app.register_blueprint(routes)
    app.register_blueprint(errors)
    error_handlers(app)

    return app
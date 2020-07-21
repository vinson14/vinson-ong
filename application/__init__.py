from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    """Initialize the core application. """
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('config.DevConfig')

    # Initialize the plugins to app
    db.init_app(app)

    # Creating the app context
    with app.app_context():

        # Import routes
        from .home import home

        # Register Blueprints
        app.register_blueprint(home.home_bp)

        return app

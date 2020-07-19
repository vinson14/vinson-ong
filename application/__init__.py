from flask import Flask


def create_app():
    """Initialize the core application. """
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('config.Config')

    # Initialize the plugins to app

    # Creating the app context
    with app.app_context():

        # Import routes
        from .home import home

        # Register Blueprints
        app.register_blueprint(home.home_bp)

        return app

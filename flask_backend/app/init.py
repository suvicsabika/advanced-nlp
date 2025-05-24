from flask import Flask
from app.routes.news_routes import news_bp


def create_app():
    """
    Creates and configures a new Flask application instance.

    This function initializes an instance of the Flask application, registers
    necessary blueprints, and prepares it to handle incoming HTTP requests.
    Typically, it is the entry point for starting the application.

    :return: A configured Flask application instance
    :rtype: Flask
    """
    app = Flask(__name__)
    app.register_blueprint(news_bp)

    return app
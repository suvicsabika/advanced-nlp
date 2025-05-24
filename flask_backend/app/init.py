from flask import Flask
from flask_cors import CORS

from app.routes.news_generation_routes import news_generation_bp
from app.routes.news_routes import news_bp


def create_app():
    """
    Creates and configures a new Flask application instance.

    This function initializes an instance of the Flask application, registers
    the necessary blueprints, and prepares it to handle incoming HTTP requests.
    Typically, it is the entry point for starting the application.

    :return: A configured Flask application instance
    :rtype: Flask
    """
    app = Flask(__name__)
    CORS(app)  # **@Divinyi: ALL CORS ORIGINS ARE ALLOWED DURING THE FRONTEND DEVELOPMENT.**

    app.register_blueprint(news_bp)
    app.register_blueprint(news_generation_bp)

    return app
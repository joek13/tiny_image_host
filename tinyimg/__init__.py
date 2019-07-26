from flask import Flask
from . import endpoints, default_config

def create_app():
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_object(default_config)
    app.config.from_pyfile("config.py")

    app.register_blueprint(endpoints.bp, url_prefix="/")

    return app

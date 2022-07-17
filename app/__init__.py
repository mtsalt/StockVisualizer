from flask import Flask

def create_app(setting=None):

    """Create an application."""

    if setting is None:
        raise ConfigUnsetException("create_app function, setting value is not set.")

    app = Flask(__name__)
    app.config.from_object(setting)

    from .views import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app

class ConfigUnsetException(Exception):
    pass
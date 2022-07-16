from flask import Flask


def create_app(debug=False):

    """Create an application."""
    app = Flask(__name__)
    app.debug = debug
    app.config['SECRET_KEY'] = 'secret!'

    from .views import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
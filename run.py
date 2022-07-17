from flask import config
from app import create_app
import app.config as conf


if __name__ == '__main__':

    # TODO: attention to setting parameter when deploying this app!
    app = create_app(setting=conf.development_conf)

    try:
        app.run()
    except Exception as e:
        print(e)
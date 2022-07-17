from flask import config
from app import create_app
from app.config import development_conf, production_conf


if __name__ == '__main__':

    # TODO: attention to setting parameter when deploying this app!
    app = create_app(setting=development_conf.Config)

    try:
        app.run()
    except Exception as e:
        print(e)
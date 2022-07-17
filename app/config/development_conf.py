from app.config import default_conf


class Config(default_conf.Config):
    SERVER_NAME = "192.168.11.16:5000"
    DEBUG = True
    SECRET_KEY = "secret!"

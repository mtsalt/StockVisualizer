from app.config import default_conf


class Config(default_conf.Config):
    SERCER_NAME = "0.0.0.0:5000"
    DEBUG = True
    SECRET_KEY = "secret!"

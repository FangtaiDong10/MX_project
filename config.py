from flask import Config

class Config(Config):
    enable_y_utc = True
    APP_NAME = "app"
    MONGODB_DB = "api"
    MONGODB_USERNAME = "root"
    MONGODB_PASSWORD = "root"
    MONGODB_HOST = "127.0.0.1"
    MONGODB_PORT = 27017
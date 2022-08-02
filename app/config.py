from flask import Config


class Config(Config):
    enable_utc = True
    APP_NAME = "app"
    MONGODB_DB = "api"
    MONGODB_USERNAME = "root"
    MONGODB_PASSWORD = "root"
    MONGODB_HOST = "127.0.0.1"
    MONGODB_PORT = 27017
    JWT_SECRET_KEY = "asjkdfhlasdjfkljaklsdjflkjasd;lf"
    ERROR_404_HELP = False
    AWS_BUCKET_NAME = "sx-spa-demo"

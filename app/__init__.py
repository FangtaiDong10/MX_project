from flask import Flask
from flask_restx import Api
from flask import Blueprint
from flask_mongoengine import MongoEngine
from flask_cors import CORS
from flask_jwt_extended import JWTManager
import logging
import os
from app.config import Config


from app.campus.controller import campus_api
from app.user.controller import auth_api, user_api, student_api, admin_api, teacher_api
from app.course.controller import course_api
from app.order.controller import order_api
from app.user import register_user_lookup

api_bp = Blueprint("api", __name__, url_prefix="/api/v1")
api = Api(api_bp)

api.add_namespace(campus_api)
api.add_namespace(auth_api)
api.add_namespace(user_api)
api.add_namespace(student_api)
api.add_namespace(admin_api)
api.add_namespace(teacher_api)
api.add_namespace(course_api)
api.add_namespace(order_api)


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Config logger
    log_path = os.path.join(app.root_path, "logs")
    if not os.path.exists(log_path):
        os.makedirs(log_path)

    file_handler = logging.FileHandler(f"{log_path}/default.log")
    file_handler.setFormatter(
        logging.Formatter("[%(asctime)s] %(levelname)s in %(module)s: %(message)s")
    )
    app.logger.addHandler(file_handler)
    app.logger.setLevel(logging.DEBUG)

    # DB
    MongoEngine(app)

    # CORS
    CORS(app)

    # JWT
    jwt = JWTManager(app)
    register_user_lookup(jwt)

    app.register_blueprint(api_bp)

    return app

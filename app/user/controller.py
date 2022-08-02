import datetime
from urllib import request
from flask_restx import Namespace, Resource
from flask import request
from .model import User, Admin, Student, Teacher, check_password, get_hashed_password
from flask_jwt_extended import create_access_token, current_user, jwt_required
from . import permission_required
from ..campus.model import Campus
from ..utils import paginate
from mongoengine import NotUniqueError

auth_api = Namespace("auth")


@auth_api.route("/login")
class Login(Resource):
    def post(self):
        username = request.json.get("username")
        password = request.json.get("password")
        if not username or not password:
            return {"message": "username or password is missing"}, 400
        user = User.objects(username=username).first_or_404(message="User not found")
        if not check_password(password, user.password):
            return {"message": "password is incorrect"}, 401

        jwt_token = create_access_token(
            identity=user.username, expires_delta=datetime.timedelta(days=30)
        )
        return {"user": user.to_dict(), "token": jwt_token}, 201


user_api = Namespace("users")


@user_api.route("/")
class UserListApi(Resource):
    @permission_required()
    def get(self):
        obj_cls = User
        if "user_type" in request.args:
            user_type = request.args["user_type"]
            if user_type == "admin":
                obj_cls = Admin
            elif user_type == "teacher":
                obj_cls = Teacher
            elif user_type == "student":
                obj_cls = Student

        # List of filters
        query = {}
        if "campus" in request.args:
            query["campus"] = request.args["campus"]

        page = request.args.get("page", 1, int)

        return paginate(obj_cls.objects(**query), page_num=page)


@user_api.route("/<username>")
class UserApi(Resource):
    @jwt_required()
    def get(self, username):
        if username != current_user.username and not isinstance(current_user, Admin):
            return {"message": "permission denied"}, 403
        return (
            User.objects(username=username)
            .first_or_404(message="User not found")
            .to_dict()
        )

    @permission_required()
    def delete(self, username):
        user = User.objects(username=username).first_or_404(message="User not found")
        if isinstance(user, Admin) and "sys_owner" not in current_user.permissions:
            return {"message": "permission denied"}, 403

        user.delete()
        return user.to_dict(), 200


student_api = Namespace("students")


@student_api.route("/")
class StudentListApi(Resource):
    def post(self):
        try:
            request_data = request.json
            request_data["password"] = get_hashed_password(request_data["password"])
            student = Student(**request_data)
            student.save()
            return student.to_dict(), 201
        except NotUniqueError:
            return {"message": "Username already exists"}, 409


admin_api = Namespace("admins")


@admin_api.route("/")
class AdminListApi(Resource):
    @permission_required("sys_owner")
    def post(self):
        try:
            request_data = request.json
            request_data["password"] = get_hashed_password(request_data["password"])
            request_data["campus"] = Campus.objects(
                id=request_data["campus"]
            ).first_or_404("Campus not found")
            admin = Admin(**request_data)
            admin.save()
            return admin.to_dict(), 201
        except NotUniqueError:
            return {"message": "Username already exists"}, 409


teacher_api = Namespace("teachers")


@teacher_api.route("/")
class TeacherListApi(Resource):
    @permission_required()
    def post(self):
        try:
            request_data = request.json
            request_data["password"] = get_hashed_password(request_data["password"])
            request_data["campus"] = Campus.objects(
                id=request_data["campus"]
            ).first_or_404("Campus not found")
            teacher = Teacher(**request_data)
            teacher.save()
            return teacher.to_dict(), 201
        except NotUniqueError:
            return {"message": "Username already exists"}, 409

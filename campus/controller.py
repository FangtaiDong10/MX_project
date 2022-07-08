from flask_restx import Namespace, Resource
from flask import jsonify, request

# work like prefix
api = Namespace('campus')

@api.route("/")
class CampusListApi(Resource):
    def get(self):
        return [
            {"name" : "monash"}
        ]
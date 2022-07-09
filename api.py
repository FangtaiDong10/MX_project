from flask import Flask
from flask_restx import Api
from flask_mongoengine import MongoEngine

from students.controller import api as student_api
from campus.controller import api as campus_api

from config import Config

import json
import datetime
from bson import ObjectId

# class CustomEncoder(json.JSONEncoder):
#     def default(self, obj):
#         if isinstance(obj, datetime.datetime):
#             return obj.isoformat()
#         elif isinstance(obj, ObjectId):
#             return str(obj)
#         else:
#             return super().default(obj )


app = Flask(__name__)
app.config.from_object(Config)
# app.json_encoder = CustomEncoder
MongoEngine(app)


api = Api(app)

# can be used as flask default blueprint purpose
api.add_namespace(student_api)

api.add_namespace(campus_api)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000, debug=True)

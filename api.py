from flask import Flask, jsonify, request
from flask_restx import Api, Resource

from students.controller import api as student_api

app = Flask(__name__)
api = Api(app)

# can be used as flask default blueprint purpose
api.add_namespace(student_api)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000, debug=True)
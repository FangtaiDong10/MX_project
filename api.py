from flask import Flask
from flask_restx import Api

from students.controller import api as student_api
from campus.controller import api as campus_api

app = Flask(__name__)
api = Api(app)

# can be used as flask default blueprint purpose
api.add_namespace(student_api)
api.add_namespace(campus_api)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000, debug=True)
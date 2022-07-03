from flask import Flask, jsonify, request
from flask_restx import Api, Resource

app = Flask(__name__)
api = Api(app)

class Student:
    def __init__(self, student_id, student_name) -> None:
        self.id = student_id
        self.name = student_name
    def to_dict(self):
        
        # return JSON data structure
        return {
            "id": self.id,
            "name": self.name
        }

# simulate a none real db
student_db = [
    Student("1","Tom"),
    Student("2","Jerry")
]


@api.route("/students")
class StudentListApi(Resource):
    def get(self):
        return jsonify([student.to_dict() for student in student_db])

    def post(self):
        # get the post request from users, and then parse the JSON data into object, which then stored in the data variable.
        data = request.json
        for student in student_db:
            if student.id == data['id']:
                return {}, 409
        
        # if the input student not exists
        # initialize a new student object with the input student id & name
        student = Student(data['id'], data['name'])
        
        # append the student database
        student_db.append(student)
        return student.to_dict(), 201





if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)
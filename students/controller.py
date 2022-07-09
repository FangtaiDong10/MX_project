from email import message
from flask import jsonify, request
from flask_restx import Namespace, Resource
from .model import Student
from campus import controller

api = Namespace('students')


# simulate a none real db
# student_db = [
#     Student("1", "Tom"),
#     Student("2", "Jerry")
# ]


@api.route("/")
class StudentListApi(Resource):
    def get(self):
        # return jsonify([student.to_dict() for student in student_db])
        return [student.to_dict() for student in Student.objects()]
        

    def post(self):
        # get the post request from users, and then parse the JSON data into object, which then stored in the data variable.
        data = request.json 

        # for student in student_db:
        #     if student.id == data['id']:
        #         return {}, 409

        # # if the input student not exists
        # # initialize a new student object with the input student id & name
        # student = Student(data['id'], data['name'])

        # # append the student database
        # student_db.append(student)
        # return student.to_dict(), 201
        student = Student()
        student.name = data['name']
        student.save()
        return student.to_dict(), 201
        

@api.route("/<student_id>")
class StudentApi(Resource):
    def get(self, student_id):
        # for student in student_db:
        #     if student.id == student_id:
        #         return student.to_dict()
        # return "", 404
        
        # check student by id
        return Student.objects(id=student_id).first_or_404(message="student not found").to_dict()
        

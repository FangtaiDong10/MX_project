print("Loading...")

from app import create_app
from app.campus.model import Campus
from app.user.model import Student, Admin, User, Teacher, get_hashed_password

create_app()

Campus.objects().delete()
User.objects().delete()

c = Campus(name="unimelb")
c.save()

admin = Admin(
    username="admin",
    password=get_hashed_password("password"),
    telephone="1234567",
    permissions=["sys_owner", "campus_admin"],
    campus=c,
)
admin.save()

student = Student(
    username="student_1",
    display_name="Tom",
    password=get_hashed_password("password"),
    telephone="1234567",
    wx="wx123",
    campus=c,
)
student.save()

teacher = Teacher(
    username="teacher_1",
    display_name="Teacher",
    password=get_hashed_password("password"),
    telephone="1234567",
    abn="xxxxxxxxxxxxxx",
    campus=c,
)
teacher.save()

from ctypes import cdll
from flask_mongoengine import Document

# import different mongoengine fields
from mongoengine.fields import (
    StringField
)

# initialize a modal
class Student(Document):
    name = StringField()

    def to_dict(self):
        return {
            "id": str(self.id),
            "name": self.name
        }


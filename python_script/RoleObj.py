
from mongoengine import *

class Role(Document):
    role = StringField()

    def to_json(self):
        return {
            "role": self.role,
        }
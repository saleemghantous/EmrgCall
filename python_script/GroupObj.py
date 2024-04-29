
from mongoengine import *

class Group(Document):
    group = StringField()

    def to_json(self):
        return {
            "group": self.group,
        }
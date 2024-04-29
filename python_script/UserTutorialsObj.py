
from mongoengine import *
from .TutorialObj import *

class UserTutorial(Document):
    userId=StringField()
    tutorial_id = ObjectIdField()
    reg_date=StringField()
    complete_date=StringField()
    status=StringField()
    
    def to_json(self):
        return {
            "userId": self.userId,
            "name":self.get_tutorial_name(),
            "reg_date": self.reg_date,
            "complete_date": self.complete_date,
            "status": self.status,
            "tutorial_id":str(self.tutorial_id)
        }
    
    
    def get_tutorial_name(self):
        tutorial=Tutorial.objects.get(id=self.tutorial_id)
        return tutorial.to_json()["name"]

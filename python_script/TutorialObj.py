
from mongoengine import *

class Tutorial(Document):
    name = StringField()
    desc=StringField()
    creation_date=StringField()
    update_date=StringField()
    reg_date=StringField()
    group_list=ListField()
    content_list=ListField()



    def to_json(self):
        return {
            "name": self.name,
            "desc":self.desc,
            "creation_date": self.creation_date,
            "update_date": self.update_date,
            "reg_date": self.reg_date,
            "group_list": self.get_group_string(),
            "content_list": self.content_list,
        }
        
    def get_group_string(self):
        return ",".join([group["label"] for group in self.group_list])
    
    def get_group_list(self):
        return self.group_list
    
    def get_content_list(self):
        return ",".join([content["label"] for content in self.content_list])
    
    

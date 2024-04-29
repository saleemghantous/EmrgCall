from mongoengine import *


class Report(Document):
    alert_target = StringField()
    alert_type = StringField()
    alert_date = StringField()
    
    
    def to_json(self):
        return {
            "alert_target": self.alert_target,
            "alert_type": self.alert_type,
            "alert_date": self.alert_date,
        }

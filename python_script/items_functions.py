from .RoleObj import *
from .GroupObj import *
from .UserObj import *
from .TutorialObj import *
from . import *
from .authentication import *
from mongoengine import *
from datetime import datetime
from .UserTutorialsObj import *
from .SendEmail import *
from .config import config
import json


def get_workder_json():
    with open("C:\dev\daily_scripts\data.json", "r") as file:
        loaded_data = json.load(file) 
        return loaded_data
    
def get_jobs_departments(data):
    print(data)
    if (check_admin(data["userSlice"]["username"], data["userSlice"]["password"])):
        return {"jobs":config["jobs"],"departments":config["departments"]}
    return {}

# users functions
def get_worker(data):
    print(data)
    if (check_admin(data["userSlice"]["username"], data["userSlice"]["password"])):
        item_list = []
        items = User.objects()
        for item in items:
            item_list.append(item.to_json())
        return {"data": item_list}
    else:
        return {}


def add_worker(data):
    # counter=0
    # for worker in get_workder_json():
    #     print(counter)
    #     new_item = User.objects(phone=worker["phone"]).first()
    #     if (not new_item):
            
    #         new_item = User(first_name=worker["first_name"],
    #                         last_name=worker["last_name"],
    #                         role=worker["role"],
    #                         phone=worker["phone"],
    #                         address=worker["address"],
    #                         department=worker["department"],
    #                         first_phase=worker["first_phase"],
    #                         second_phase=worker["second_phase"])
    #         new_item.save()
    #         counter+=1
    if (check_admin(data["userSlice"]["username"], data["userSlice"]["password"])):
        new_item = User.objects(phone=data["itemData"]["phone"]).first()
        if (not new_item):
            
            new_item = User(first_name=data["itemData"]["first_name"],
                            last_name=data["itemData"]["last_name"],
                            role=data["itemData"]["role"],
                            phone=data["itemData"]["phone"],
                            address=data["itemData"]["address"],
                            department=data["itemData"]["department"],
                            first_phase=data["itemData"]["first_phase"],
                            second_phase=data["itemData"]["second_phase"]
                            )
            new_item.save()
            return {"comment": f"ה{data['hebrewName']} נוסף בהצלחה", "result": "success"}
        else:
            return {"comment": f"ה{data['hebrewName']} מוגדר במערכת כבר", "result": "error"}
    else:
        return {"result": "error", "comment": "השתבש משהו בזמן ההוספה"}


def edit_worker(data):
    if (check_admin(data["userSlice"]["username"], data["userSlice"]["password"])):
        item = User.objects(phone=data["itemData"]["phone"]).first()
        if (item): 
            item.update(**data["itemData"])
            return {"result": "success", "comment": f"{data['hebrewName']} עודכן בהצלחה"}
    return {"result": "error", "comment": "השתבש משהו בזמן העדכון"}


def delete_worker(data):
    # item = User.objects()
    # item.delete()
    if (check_admin(data["userSlice"]["username"], data["userSlice"]["password"])):
        item = User.objects(phone=data["row"]["phone"]).first()
        if (item):
            item.delete()
            return {"result": "success", "comment": f"ה{data['hebrewName']} נמחק בהצלחה"}
    return {"result": "error", "comment": "השתבש משהו בזמן המחיקה"}



def send_alert(data):
    
    new_item = User.objects(phone=data["itemData"]["phone"]).first()

    print(data)
    return {}
    


def get_user_tmp(userId):
    user=User.objects(userId=userId).first()
    return user.to_json() 



def send_email(data):
    if (check_admin(data["userSlice"]["userId"], data["userSlice"]["password"])):
        tutotial=Tutorial.objects(name=data["row"]["name"]).first()
        if(tutotial):
            tutorial_id=tutotial.id
            userTutorial=UserTutorial.objects(tutorial_id=tutorial_id)
            user_counter=0
            for uTutorial in userTutorial:
                if(uTutorial.to_json()["status"]!="בוצע"):
                    user_json=get_user_tmp(uTutorial.to_json()["userId"])
                    try:
                        send_email_func(user_json,tutotial.to_json())
                        user_counter=user_counter+1
                    except:
                        return {"result":"error","message":"השתמש משהו במערכת"}
        return {"result":"success","message":f"תזכורת נשלחה בהצלחה ל {str(user_counter)} משתמשים"}
    return {"result":"error","message":"השתמש משהו במערכת"}
    
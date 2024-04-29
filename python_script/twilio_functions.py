from twilio.twiml.voice_response import Gather, Say, VoiceResponse
from twilio.twiml.messaging_response import MessagingResponse
from twilio.rest import Client
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
from flask import Flask, request


account_sid = ''
auth_token = ''
from_number = "+97293762583"
client = Client(account_sid, auth_token)
action = "https://cdc2-2a06-c701-78c1-b700-bc77-7486-7420-f84b.ngrok-free.app/api/handle_key"

mp3_dict = {
    "limited_real": 'https://sapphire-wolf-8672.twil.io/assets/staff_real.mp3',
    "limited_real_res_1": "https://sapphire-wolf-8672.twil.io/assets/staff_real_res_1.mp3",
    "limited_real_res_2": "https://sapphire-wolf-8672.twil.io/assets/staff_real_res_2.mp3",
    "limited_real_res_2": "https://sapphire-wolf-8672.twil.io/assets/staff_real_res_3.mp3",
}


history = {
    "limited": {
        "real": [],
        "exercise": []
    },
    "extended": {
        "real": [],
        "exercise": []
    }
}


def send_alert(data):
    if (data["alertTarget"] == "limited" and data["alertType"] == "real"):
        users = User.objects(first_phase="כן")
        for user in users:
            send_to_staff(user.to_json()["phone"], alert_target=data["alertTarget"], alert_type=data["alertType"])
            print(user.to_json())
    return {}


def send_to_staff(to, alert_target, alert_type):
    print(to, alert_target, alert_type)
    # Replace with your own Twilio phone numbers
    to_number = '+972'+str(to)[1:]
    # Create a TwiML response
    twiml_response = VoiceResponse()

    # Use Gather to collect user input
    gather = Gather(numDigits=1, action=action, method='POST', timeout=15)

    gather.play(mp3_dict[f"{alert_target}_{alert_type}"])
    twiml_response.append(gather)

    # Use the generated TwiML in the call
    call = client.calls.create(
        twiml=str(twiml_response),  # Convert TwiML to string
        to=to_number,
        from_=from_number,
    )

    if (not to in history[alert_target][alert_type]):
        history[alert_target][alert_type].append(str("+972"+to[1:]))
    return str(call.sid)


def get_alert_info(data):
    for outer_key, inner_dict in history.items():
        for inner_key in inner_dict:
            if data["Called"] in inner_dict[inner_key]:
                return outer_key, inner_key
    return -1,-1


def handle_key(data):
    alert_target, alert_type = get_alert_info(data)
    
    if alert_target != -1 and alert_type != -1:
        
        digit_pressed = data.get('Digits')
        twiml_response = VoiceResponse()
        
        if digit_pressed == '1':
            twiml_response.play(mp3_dict[f"{alert_target}_{alert_type}_res_1"])
        elif digit_pressed == '2':
            twiml_response.play(mp3_dict[f"{alert_target}_{alert_type}_res_2"])
        elif digit_pressed == '3':
            twiml_response.play(mp3_dict[f"{alert_target}_{alert_type}_res_3"])
        else:
            # Use Gather to collect user input again
            gather = Gather(numDigits=1, action=action, method='POST', timeout=15)
            gather.play(mp3_dict[f"{alert_target}_{alert_type}"])
            twiml_response.append(gather)
            return str(twiml_response)
        
        history[alert_target][alert_type].remove(data["Called"])
        return str(twiml_response)
    return {}

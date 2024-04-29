from flask import Flask,send_file, send_from_directory, request,Response
import os
import json
from mongoengine import *
from flask_cors import CORS
from python_script import login as login
from python_script import twilio_functions as twilio_fn
from python_script import items_functions as items_func
import requests
from pymongo.mongo_client import MongoClient
import pymongo 
import os
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from twilio.rest import Client
from twilio.request_validator import RequestValidator


# Twilio credentials
account_sid = ''
auth_token = ''
twilio_phone_number = 'whatsapp:+14159692549'
recipient_number = 'whatsapp:+972545943983'  # Replace with the recipient's phone number

# Create a Twilio client
client = Client(account_sid, auth_token)


uri="mongodb://admin:X8NORPwnCNZ0dMzU@ac-e46mcen-shard-00-00.pgoqiio.mongodb.net:27017,ac-e46mcen-shard-00-01.pgoqiio.mongodb.net:27017,ac-e46mcen-shard-00-02.pgoqiio.mongodb.net:27017/?ssl=true&replicaSet=atlas-avi7im-shard-0&authSource=admin&retryWrites=true&w=majority"
validator = RequestValidator(auth_token)

app = Flask(__name__, static_folder="build")
cors = CORS(app)
app.config["CORS-HEADERS"] = "Content-Type"




host=f"mongodb+srv://emrgcall.pgoqiio.mongodb.net/?authSource=%24external&authMechanism=MONGODB-X509&retryWrites=true&w=majority"
connect(db='emrgcall',host=uri)
"hospitalemergencycall@gmail.com"



    
@app.route("/", defaults={"path": ""})
@app.route("/<path:path>")
def index(path):
    if (path != "" and os.path.exists(app.static_folder + "/" + path)):
        return send_from_directory(app.static_folder + "/", path)
    else:
        return send_from_directory(app.static_folder, "index.html")

@app.route("/api/login", methods=["POST"])
def login_request():
    data = dict(json.loads(request.data.decode('utf-8')))
    print(data)
    return login.login_request(data)


@app.route("/api/mp3", methods=["POST"])
def mp3():
    print(request.data)
    mp3_file_path = 'C:/Users/Saleem/Desktop/exercise.mp3'
    # Return the MP3 file using Flask's send_file function
    return {}

@app.route("/api/send_email", methods=["POST"])
def send_email():
    data = dict(json.loads(request.data.decode('utf-8')))
    return items_func.send_email(data)

# users functions
@app.route("/api/add_worker", methods=["POST"])
def add_worker():
    data = dict(json.loads(request.data.decode('utf-8')))
    return items_func.add_worker(data)

@app.route("/api/get_worker", methods=["POST"])
def get_worker():
    data = dict(json.loads(request.data.decode('utf-8')))
    return items_func.get_worker(data)

@app.route("/api/edit_worker", methods=["POST"])
def edit_worker():
    data = dict(json.loads(request.data.decode('utf-8')))
    return items_func.edit_worker(data)

@app.route("/api/delete_worker", methods=["POST"])
def delete_worker():
    data = dict(json.loads(request.data.decode('utf-8')))
    return items_func.delete_worker(data)


@app.route("/api/get_jobs_departments", methods=["POST"])
def get_jobs_departments():
    data = dict(json.loads(request.data.decode('utf-8')))
    return items_func.get_jobs_departments(data)


# user tutorial
@app.route("/api/delete_user_tutorials", methods=["POST"])
def delete_user_tutorials():
    data = dict(json.loads(request.data.decode('utf-8')))
    return items_func.delete_user_tutorials(data)


# user tutorial
@app.route("/api/send_alert", methods=["POST"])
def send_alert():
    data = dict(json.loads(request.data.decode('utf-8')))
    # twilio_fn.test()
    return twilio_fn.send_alert(data)

# user tutorial
@app.route("/api/handle_key", methods=["POST"])
def handle_key():
    return twilio_fn.handle_key(request.form.to_dict())


@app.route("/api/get_information", methods=["GET"])
def get_information():
    data = dict(json.loads(request.args))
    return data

@app.route('/whatsapp', methods=['POST'])
def reply():
    print("saleem")
    # Validate Twilio request signature
    is_valid_request = validator.validate(
        request.url,
        request.form,
        request.headers.get('X-Twilio-Signature', '')
    )

    if not is_valid_request:
        exit(403, 'Invalid Twilio request signature')

    # Rest of your code
    message = request.form.get('Body').lower()
    if message:
        return respond(f'Thank you for your message! A member of our team will be in touch with you soon.')
    else:
        return "No message received."
    
    
def respond(message):
    response = MessagingResponse()
    response.message(message)
    return str(response)


# app.run(port=5050, debug=True)


port = int(os.environ.get('PORT', 5050))  # Get the port from the environment or use 5000
app.run( port=port)
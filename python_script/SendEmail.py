import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from .config import *

# Email configuration
sender_email = config["email"]
sender_password = config["app_password"]

def send_email_func(user_json, tutorial_json):
    
    subject = "תזכורת - מערכת לומדות - בית חולים"
    body = f"""<div dir="rtl">שלום {user_json["first_name"]} {user_json["last_name"]},
    <br/>
    צריך להשלים את הלומדה - {tutorial_json["name"]} - בהקדם האפשרי.
    <br/>
    תודה רבה</div>
    """

    # Create the MIME object
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = user_json["email"]
    message["Subject"] = subject
    message.attach(MIMEText(body, "html", _charset="utf-8"))  # Set the content type to HTML

    # Connect to Gmail's SMTP server
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(sender_email, sender_password)

    # Send the email
    server.sendmail(sender_email, user_json["email"], message.as_string())

    # Close the server connection
    server.quit()


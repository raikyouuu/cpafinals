import smtplib
from email.mime.text import MIMEText
import json

def get_owner_email(apartment):
    return apartment.get('email')

def send_email(to_email, message_body):
    sender_email = "raizenaaroncpa@gmail.com" 
    sender_password = "ljgy xgop ymrx ytef"  

    subject = "Regarding Your Apartment Listing"
    body = message_body

    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender_email
    msg['To'] = to_email

    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls() 
            server.login(sender_email, sender_password)
            server.send_message(msg)
        print(f"\n Email sent successfully to {to_email}!")
    except Exception as e:
        print(f"\n Failed to send email. Error: {e}")

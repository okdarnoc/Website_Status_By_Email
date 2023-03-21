import requests
import smtplib
from email.mime.text import MIMEText
import yaml
import os

# Prompt the user to create the config file if it doesn't exist
if not os.path.exists('config.yml'):
    sender_email = input("Enter sender email address: ")
    recipient_email = input("Enter recipient email address: ")
    password = input("Enter email password: ")
    urls = input("Enter URLs to check (separated by commas): ").split(',')
    config = {
        'sender_email': sender_email,
        'recipient_email': recipient_email,
        'password': password,
        'urls': urls
    }
    with open('config.yml', 'w') as f:
        yaml.safe_dump(config, f)
else:
    # Read the configuration file
    with open('config.yml') as f:
        config = yaml.safe_load(f)

# Check the status of each URL
statuses = []
for url in config['urls']:
    try:
        response = requests.get(url)
        if response.status_code == 200:
            statuses.append("SUCCESS: " + url + " is up and running!")
        else:
            statuses.append("WARNING: " + url + " returned a status code of " + str(response.status_code))
    except requests.exceptions.RequestException as e:
        statuses.append("ERROR: " + url + " is down. Exception: " + str(e))

# Create the email message
message = MIMEText("\n".join(statuses))
message["Subject"] = "Daily_Website_Status_Check"
message["From"] = config['sender_email']
message["To"] = config['recipient_email']

# Send the email
with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
    server.login(config['sender_email'], config['password'])
    server.sendmail(config['sender_email'], config['recipient_email'], message.as_string())

print("Email sent!")

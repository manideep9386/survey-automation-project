import smtplib
import pandas as pd
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Load recipients
recipients = pd.read_csv("responses.csv")

# Email configuration
sender_email = "manideepreddyputta@gmail.com"
password = "qtrf fapy ociv sfej"  # Use environment variable in real apps

# Email content
subject = "We value your feedback!"
body = """
Dear Customer,

Thank you for your recent purchase. Please take a moment to complete this short survey.

[Insert Link Here]

Best regards,  
Manideep Reddy Putta 
"""

# Send emails
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(sender_email, password)

for _, row in recipients.iterrows():
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = row['email']
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))
    server.sendmail(sender_email, row['email'], msg.as_string())
    print(f"Email sent to {row['email']}")

server.quit()
import os
from dotenv import load_dotenv

load_dotenv()

sender_email = os.getenv("EMAIL")
password = os.getenv("APP_PASSWORD")

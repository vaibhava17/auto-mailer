import os
import smtplib
from email.message import EmailMessage
from email.mime.base import MIMEBase
from email import encoders
import pandas as pd
from dotenv import load_dotenv
import json

load_dotenv()

with open('content.json', 'r') as file:
    content = json.load(file)

LOGIN = os.getenv('LOGIN')
PASSWORD = os.getenv('PASSWORD')
EMAIL_SUBJECT = os.getenv('EMAIL_SUBJECT')
EMAIL_FROM = os.getenv('EMAIL_FROM')
EMAIL_ATTACHMENT = os.getenv('EMAIL_ATTACHMENT')
CSV_FILE = os.getenv('CSV_FILE')

def load_recipients(csv_file):
    df = pd.read_csv(csv_file)
    return df

def create_email(subject, body, to_email, from_email):
    msg = EmailMessage()
    msg['Subject'] = subject
    msg['From'] = from_email
    msg['To'] = to_email
    msg.set_content(body)
    msg.make_mixed()
    return msg

def attach_pdf(msg, pdf_file):
    with open(pdf_file, 'rb') as f:
        mime = MIMEBase('application', 'octet-stream')
        mime.set_payload(f.read())
        encoders.encode_base64(mime)
        mime.add_header('Content-Disposition', f'attachment; filename="{pdf_file}"')
        msg.attach(mime)

def send_email(msg, smtp_server, smtp_port, login, password):
    with smtplib.SMTP_SSL(smtp_server, smtp_port) as server:
        server.login(login, password)
        server.send_message(msg)


def main():
    subject = EMAIL_SUBJECT
    from_email = EMAIL_FROM
    pdf_file = EMAIL_ATTACHMENT
    csv_file = CSV_FILE

    df = load_recipients(csv_file)

    smtp_server = 'smtp.gmail.com'
    smtp_port = 465
    login = LOGIN
    password = PASSWORD

    for index, row in df.iterrows():
        to_email = row['email']
        name = row['name']
        body = f"Hi {name},\n\n{content['body']}"

        msg = create_email(subject, body, to_email, from_email)

        attach_pdf(msg, pdf_file)

        send_email(msg, smtp_server, smtp_port, login, password)
        print(f"Email sent to {name} ({to_email})")

if __name__ == '__main__':
    main()

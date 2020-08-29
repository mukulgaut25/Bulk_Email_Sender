from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import argparse

#variables
lst = []

#function
def sender():
    message["Subject"] = "Bulk Email Sender"  # your subject
    message.attach(MIMEText("Your text message"))
    with smtplib.SMTP(host=args.server, port=587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.login("email_address", "password")             # your fake email and password from which you wanna to send the email
        smtp.send_message(message)
        print("Sent....")

#argument passing
my_parser = argparse.ArgumentParser()

my_parser.add_argument("-file", help="Enter the email file name", required=True)
my_parser.add_argument("--target", help="Specify the targeted email address", required=True)
my_parser.add_argument("-server", help="Enter smtp server name like smtp.gmail.com", required=True)
my_parser.add_argument("-sender", help="Specify sender name", default="Bot")

args = my_parser.parse_args()

if args.file is not None:
    with open(args.file, "r") as a_file:
        for line in a_file:
            stripped_line = line.strip()
            message = MIMEMultipart()
            message["From"] = args.sender  # your sender name
            message["To"] = stripped_line
            sender()

elif args.target is not None:
    message = MIMEMultipart()
    message["From"] = args.sender  # your sender name
    message["To"] = args.target
    sender()






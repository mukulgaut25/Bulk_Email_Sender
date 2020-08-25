from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.base import MIMEBase
from email import encoders

import smtplib
lst = []

def my_attachement():

#make sure file is in the current directory from which you are running this script
     file_name = str(input("Enter File name: "))
     with open(file_name, "rb") as attachment:
        part = MIMEBase("application", "octet-stream")      #The content type "application/octet-stream" means that a MIME attachment is a binary file
        part.set_payload(attachment.read())
        encoders.encode_base64(part)

    # Adding header
     part.add_header(
        "Content-Disposition",
        f"attachment; file_name= {file_name}",
     )


     message.attach(part)                               #Add attachment to your message and convert it to string

def my_image():
    # make sure that image is also in same directory as script
    image_name = str(input("Enter image name: "))
    fp = open(image_name, 'rb')
    image = MIMEImage(fp.read())
    fp.close()

    # Specify the  ID according to the img src in the HTML part
    image.add_header('Content-ID', '<Mailtrapimage>')
    message.attach(image)

try:
    attachement = str(input("Did you want to send attachement [Yes/No]: "))
    image = str(input("Did you want to send image [Yes/No]: "))
    email_names = int(input("Enter number of email addresses: "))
except:
  print("An exception occurred")

# iterating till the range
for i in range(0, email_names):
    email = str(input("Email Address: "))
    lst.append(email)                               #appending email into lst list

for name in lst:
    message = MIMEMultipart()
    if attachement == "Yes" or attachement == "yes":
        my_attachement()
    if image == "Yes" or image == "yes":
        my_image()
    if (attachement == "no" or attachement == "No") and (image == "no" or image == "No"):
        print("No attachement or image is selected")

    message["From"] = "Sender Name"                 #your sender name
    message["To"] = name
    message["Subject"] = "Bulk email sender"                     #your subject
    message.attach(MIMEText("Your text messages"))
    with smtplib.SMTP(host="smtp.gmail.com",port=587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.login("youremailaddress","password")
        smtp.send_message(message)
        print("Sent....")


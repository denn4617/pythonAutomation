import smtplib, ssl
from getpass import getpass

with open("list.txt", "r") as fil:
    text = fil.read()

port = 587  # For starttls
smtp_server = "smtp.gmail.com"
sender_email = "dkilic5@gmail.com"
receiver_email = "dkilic5@gmail.com"
subject = 'Indkoebsliste'
body = text
password = getpass()



email_text = """\
From: %s
To: %s
Subject: %s

%s
""" % (sender_email, receiver_email, subject, body)

context = ssl.create_default_context()
with smtplib.SMTP(smtp_server, port) as server:
    server.ehlo()  # Can be omitted
    server.starttls(context=context)
    server.ehlo()  # Can be omitted
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, email_text)
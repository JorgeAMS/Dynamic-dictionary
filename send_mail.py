import datetime as dt
import time
import smtplib

def send_email():
    SERVER = "smtp-mail.outlook.com"
    FROM = "jorgea-moraless@unilibre.edu.co"
    TO = ["jamorales516@outlook.com"] # must be a list

    SUBJECT = "Test"
    TEXT = "Hello World!"

    # Prepare actual message
    message = """From: %s\r\nTo: %s\r\nSubject: %s\r\n\

    %s
    """ % (FROM, ", ".join(TO), SUBJECT, TEXT)

    # Send the mail
    import smtplib
    server = smtplib.SMTP(SERVER)
    server.login("MrDoe", "PASSWORD")
    server.sendmail(FROM, TO, message)
    server.quit()

def send_email_at(send_time):
    time.sleep(send_time.timestamp() - time.time())
    send_email()
    print('email sent')

first_email_time = dt.datetime(2018,8,26,3,0,0) # set your sending time in UTC
interval = dt.timedelta(minutes=2*60) # set the interval for sending the email

send_time = first_email_time
while True:
    send_email_at(send_time)
    send_time = send_time + interval
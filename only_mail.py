import datetime as dt
import time
import smtplib

def send_email():
    HOST = "smtp.gmail.com"
    PORT = "465"
    FROM = "jamorales516gm@gmail.com"
    TO = ["jorgea-moraless@unilibre.edu.co"] # must be a list

    SUBJECT = "Test"
    TEXT = "Hello World!"

    # Prepare actual message
    message = """From: %s\r\nTo: %s\r\nSubject: %s\r\n\

    %s
    """ % (FROM, ", ".join(TO), SUBJECT, TEXT)

    # Send the mail
    try:
        import smtplib
        server = smtplib.SMTP_SSL(HOST)
        server.starttls()
        server.login("jamorales516gm@gmail.com", "")
        server.sendmail(FROM, "jorgea-moraless@unilibre.edu.co", message)
        server.quit()
        return 'Success' 
    except Exception as e:
        return e



if __name__ == "__main__":
    print(send_email())
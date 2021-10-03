import smtplib

def send_email(message):
    #update the variables line 5-8 below with your details
    user = 'enter the from email address here'
    pwd = 'enter your password here'
    recipient = 'enter the to email address here'
    subject = 'DMV - There is an appointment'

    FROM = user
    TO = recipient if isinstance(recipient, list) else [recipient]
    SUBJECT = subject
    TEXT = body

    message = """From: %s\nTo: %s\nSubject: %s\n\n%s
    """ % (FROM, ", ".join(TO), SUBJECT, TEXT)
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.login(user, pwd)
        server.sendmail(FROM, TO, message)
        server.close()
        print('successfully sent email')
    except:
        print('failed to send email')
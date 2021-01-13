# Code can be used with assistant.py to send mails

import smtplib
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('XYZ@gmail.com', 'pass')
    server.sendmail('XYZ@gmail.com', to, content)
    server.close()
sendEmail('XYZ@gmail.com',"this is test mail")

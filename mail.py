import smtplib
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('sudhanshudekate7@gmail.com', 'pass')
    server.sendmail('sudhanshudekate7@gmail.com', to, content)
    server.close()
sendEmail('sudhanshudekate8@gmail.com',"this is test mail")
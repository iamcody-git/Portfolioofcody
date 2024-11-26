import smtplib, ssl
import os

def send_email(message):
    host = "smtp.gmail.com"
    port = 465
    
    username = "adhikariprashant009@gmail.com"
    password = os.getenv("PASSWORD") 
    # password is genrated from the gmail account app password section and that password is store in evn varaible 
    
    receiver = "iamcody.github@gmail.com"
    context = ssl.create_default_context()
    
    with smtplib.SMTP_SSL(host,port, context=context) as server:
        server.login(username, password)
        server.sendmail(username,receiver,message)
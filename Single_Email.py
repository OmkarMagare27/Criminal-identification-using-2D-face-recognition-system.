#for single email
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
s = smtplib.SMTP(host='smtp.gmail.com', port=587) #simple mail tranfer protocall
s.starttls()
s.login("criminaldetectiondemo@gmail.com", "Criminal@123")
def sendEmail(email,sms):
    
# For each contact, send the email:
    msg = MIMEMultipart()       # create a message

    # setup the parameters of the message
    msg['From']="criminaldetectiondemo@gmail.com"
    msg['To']=email
    msg['Subject']="Mail From Criminal Alert System"

    # add in the message body
    msg.attach(MIMEText(sms, 'plain'))
    print(msg)
    # send the message via the server set up earlier.
    s.send_message(msg)

    

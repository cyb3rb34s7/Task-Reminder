import schedule 
import time

import smtplib

from twilio.rest import Client 

	

def sendEmail():
	sender = "anyemailaddress"  #Put any spare email address here from which you want to recieve email notification
	recipient = "youremail"   #Put your main email address here where you want to recieve notification
	password= "password"      #put the password of sender email (Dont worry its your code so it wont leak. Plus youre using SSL encryption)
	subject = "Reminder email For your Lab " # Customize This and text field according to your needs
	text= "Please attend your lab session ASAP \n "
	smtp_server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
	smtp_server.login(sender, password)
	message = "Subject: {}\n\n{}".format(subject, text)
	smtp_server.sendmail(sender, recipient, message)
	smtp_server.close()


def whatsappNotification():
	account_sid = 'twilio-SID'   #paste your twilio account SID and token copied from your twilio console
	auth_token = 'twilio-token' 
	client = Client(account_sid, auth_token)
	message = client.messages.create( 
                              from_='whatsapp:#######',   #put the number you got in twilio that you used to send verification
                              body='Please attend your lab session ASAP \n ',      
                              to='whatsapp:###########'  #Put your Whatsapp number here
                          ) 
	print(message.sid)



schedule.every().monday.at("13:50").do(sendEmail)   #Modify these Schedules according to your needs Change Day,Time
schedule.every().monday.at("13:50").do(whatsappNotification)
#schedule.every().wednesday.at("13:50").do(sendEmail)
#schedule.every().wednesday.at("13:50").do(whatsappNotification)
#schedule.every(5).seconds.do(whatsappNotification)     #This is to send whatsapp notification every 5 seconds


while True:
	schedule.run_pending()
	time.sleep(1)

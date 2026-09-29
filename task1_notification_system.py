#Notification system -Hierarchical inheritance+Method overriding+Polymorphism
class Notification:
    def __init__(self,recipient):
        self.recipient=recipient
    def send(self):
        print("Sending notification to..")
class EmailNotification(Notification):
    def send(self):
        print("Sending Email to",self.recipient)
class SMSNotification(Notification):
    def send(self):
        print("Sending SMS to",self.recipient)
email_noti=EmailNotification("user@example.com")
sms_noti=SMSNotification("0812345678")
notis=[email_noti,sms_noti]
for noti in notis:
    noti.send()
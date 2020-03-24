from twilio.rest import Client
from credentials import account_sid

account_sid = 'AC8cbdcbcba0273f901fbd22c69f85395d'
auth_token = 'dc8197ad8409a9bb1fb46c1941217043'
my_cell = '+821047244188'  
my_twilio = '+12058435576'

client = Client(account_sid, auth_token)

my_msg = ''.join(['silly bob\n' for i in range(10)])

message = client.messages.create(to=my_cell, from_=my_twilio,
                                 body=my_msg)

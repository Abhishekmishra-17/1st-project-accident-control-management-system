# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = 'ACbaf4d39ddf69801f4255590968c564b8'
auth_token = 'a9b1ac8c0d10834190e18340473dc9df'
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="Join Earth's mightiest heroes. Like Kevin Bacon.",
                     from_='+14012576091',
                     to='+918874036548'
                 )

print(message.sid)

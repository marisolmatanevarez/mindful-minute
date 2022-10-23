import os, sqlite3, sys
from twilio.rest import Client
from models import Quote, Meme, Message
import random

account_sid = os.environ['TWILIO_ACCOUNT_SID']
api_key = os.environ['TWILIO_API_KEY']
api_secret = os.environ['TWILIO_API_SECRET']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
our_phone = os.environ['TWILIO_PHONE']

twclient = Client() #fill in later

conn = sqlite3.connect("database.db")

if __name__ == '__main__':
    time = sys.argv[1]
    #payload = sys.argv[2]
    payload = "Mindful Moments: just checking in! "

    i = random.randint(0, 2)
    if i == 0:
        payload += Quote.get_random()
    elif i == 1:
        payload += Meme.get_random()
    else:
        payload += Message.get_random()

    query = "SELECT phone FROM Users WHERE time = ?"
    for row in conn.execute(query, time).fetchall():
        twclient.messages.create(
            body=payload,
            from_=our_phone,
            to=row[0]
        )

    conn.close()
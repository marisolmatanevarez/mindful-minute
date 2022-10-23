import os, sqlite3, sys
from twilio.rest import Client

account_sid = os.environ['TWILIO_ACCOUNT_SID']
api_key = os.environ['TWILIO_API_KEY']
api_secret = os.environ['TWILIO_API_SECRET']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
our_phone = os.environ['TWILIO_PHONE']

twclient = Client() #fill in later

conn = sqlite3.connect("database.db")

if __name__ == '__main__':
    time = sys.argv[1]

    query = "SELECT phone FROM Users WHERE time = :time"
    for row in conn.execute(query, time=time):
        twclient.messages.create(
            body="test",
            from=our_phone,
            to=row[0]
        )

    conn.close()
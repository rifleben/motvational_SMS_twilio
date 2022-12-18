from quote_data import quotes
import datetime as dt
import random
import time
from twilio.rest import Client

account_sid = "YOUR TWILIO SID"
auth_token = "YOUR TWILIO AUTH TOKEN"
client = Client(account_sid, auth_token)


def is4_30p():
    """Check if it's 4:30pm"""
    now = dt.datetime.now()
    if now.hour == 16 and now.minute == 30:
        return True
    else:
        return False


while True:
    # Check every 60 seconds if it's 4:30pm
    if is4_30p():
        quote = random.choice(quotes)
        message = client.messages.create(
            body=f"{quote['text']} - {quote['author']}",
            from_="YOUR TWILIO NUMBER",
            to="+RECIPIENT_NUMBER"
        )
        print(message.status)
    # Once the message is sent, we can loop once every 24 hours instead of every 60 seconds:
        time.sleep(60 * 60 * 24)
    else:
        time.sleep(60)

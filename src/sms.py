# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client

def send(body='Some body', to=''):
    # Your Account Sid and Auth Token from twilio.com/console
    # DANGER! This is insecure. See http://twil.io/secure
    account_sid = os.getenv("ACCT_SID")
    auth_token = os.getemv("TOKEN")
    client = Client(account_sid, auth_token)

    message = client.messages \
                    .create(
                        body=body,
                        from_='+12058755998',
                        to='+'+to
                    )

    print(message.sid)
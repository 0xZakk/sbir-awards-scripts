import requests
from time import sleep
import os
from twilio.rest import Client

account_sid = os.environ.get('TWILIO_ACCOUNT_SID')
auth_token = os.environ.get('TWILIO_AUTH_TOKEN')
twilio_client = Client(account_sid, auth_token)

for i in range(0, 5):
# for i in range(0, 17628):
    res = requests.get(f"https://www.sbir.gov/sbirsearch/award/all?page={i}")
    f = open(f"./html/page{i}.html", 'a')
    f.write(res.text)
    f.close()
    sleep(1)

message = twilio_client.messages.create(
    body="Finished pulling Pages of grants",
    from_="+17027663746",
    to="+17132809889"
)
import os
import glob
import json
from bs4 import BeautifulSoup
from twilio.rest import Client

account_sid = os.environ.get('TWILIO_ACCOUNT_SID')
auth_token = os.environ.get('TWILIO_AUTH_TOKEN')
twilio_client = Client(account_sid, auth_token)

samples = glob.glob("../pull_paginated_pages_of_awards/html/*.html")

for i, sample in enumerate(samples):
    with open(sample) as f:
        grants = []
        soup = BeautifulSoup(f, 'html.parser')
        resultsList = soup.select_one('.search-results')
        titleNodes = resultsList.select('h3.title a')
        for title in titleNodes:
            grants.append({
                "title": title.get_text(),
                "detail_url": f"http://www.sbir.gov{title['href']}",
                "sbir_id": title['href'][-7:]
            })
            
        with open(f"./grants/{i}.json", 'w+') as jsonFile:
            json.dump(grants, jsonFile, indent=2)

message = twilio_client.messages.create(
    body="finished extracting grant summaries as json",
    from_="+17027663746",
    to="+17132809889"
)
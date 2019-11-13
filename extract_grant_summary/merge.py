import os
import glob
import json
from bs4 import BeautifulSoup
from twilio.rest import Client


grants = glob.glob("./grants/*.json")

for i, grant_set in enumerate(grants):
    with open('./grants.json', 'r+') as grants:
        with open(grant_set, 'r') as grant_set:
            existing_grants = json.load(grants)
            new_grants = json.load(grant_set)

            existing_grants.extend(new_grants)

            with open('./grants.json', 'w+') as f:
                json.dump(existing_grants, f, indent=2)

#!/usr/bin/env pipenv run python

import json
import os
import requests
import glob
from time import sleep
from bs4 import BeautifulSoup

samples = glob.glob('./extract_grant_summary/samples/*.json')

for i, sample in enumerate(samples):
    with open(sample) as sample_awards:
        sample_awards = json.load(sample_awards)
        awards = []

        for sample_award in sample_awards:
            url = f"https://www.sbir.gov/api/awards/{sample_award['sbir_id']}.json"
            res = requests.get(url)
            awards.append(res.json())
            sleep(1)

        with open(f"./get_grant_data/grants/{i}.json", 'w+') as f:
            json.dump(awards, f, indent=2)


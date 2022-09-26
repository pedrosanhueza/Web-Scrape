import http.client
import json
import pandas as pd
from bs4 import BeautifulSoup
from datetime import datetime

## REQUEST DATA FROM API ENDPOINT
conn = http.client.HTTPSConnection("web.byui.edu")
conn.request("GET", "/studentemployment/api/jobs")
res = conn.getresponse()
data = res.read()
info = data.decode("utf-8")
responseObject = json.loads(info)

data_jobs = pd.DataFrame(responseObject)
data_jobs['URL'] = data_jobs.jobID.apply(lambda x: f'https://web.byui.edu/StudentEmployment/job/{x}')

data = data_jobs
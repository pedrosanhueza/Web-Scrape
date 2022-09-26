import requests
import pandas as pd
from bs4 import BeautifulSoup

url = 'http://web.byui.edu/studentemployment/api/jobs'

response = requests.get(url)

object = response.json()

data_jobs = pd.DataFrame(object)

data_jobs['URL'] = data_jobs.jobID.apply(lambda x: f'https://web.byui.edu/StudentEmployment/job/{x}')

data_jobs['description'] = data_jobs['description'].apply(lambda x: [p.text.strip() for p in BeautifulSoup(x).find_all('p') if p.text.strip() != ''])

data = data_jobs
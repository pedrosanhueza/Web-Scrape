import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime

url = 'https://www.irvinespectrumcenter.com/shopping/stores?filter=all'

response = requests.get(url)

soup = BeautifulSoup(response.text)

rows=[]

companies = soup.find('div',{'class':'directory__listings'}).find_all('div',{'class':'directory__listings__column'})[1:]

for company in companies:

    row={}

    row['Name']      =  company['data-name']
    row['Features']  =  company['data-listing-row'].split(' ')
    row['Phone']     =  company.find('a').find('div',{'class':'directory__listing__phone'}).text
    row['Suite']     =  company['data-suite']
    row['Logo_url']  =  company.find('a').find('img')['src']
    row['Category1'] =  company.find('a')['href'].split('/')[1]
    row['Category2'] =  company.find('a')['href'].split('/')[2]
    row['Status']    =  company['data-status']
    row['Deal']      =  company['data-deals']

    rows.append(row)

data = pd.DataFrame(rows) # build a data frame from the list of dictionaries
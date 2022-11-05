import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime
import plotly.express as px

# ----------------------------------- 12 sec: Build Tabular Data ----------------------------------- #

page = 1
rows = []
rows_votes = []
url_base = 'feedback.mutual.app'

while page:
    url = f'https://{url_base}/?page={page}&order=popular&filter=all#controls' # url for each page. only change the page number
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # List of dict: mulitple attributes
    info = soup.find_all('div',{'class':'sInfo'})
    for attribute in info:
        row = {}
        row['page'] = page
        row['id'] = attribute.find('a')['href'].split('/')[2]
        row['suggestion'] = attribute.find('a')['href'].split('/')[-1].replace('-',' ').capitalize()
        row['author'] = attribute.find_all('strong')[0].get_text()
        start = attribute.find_all('span')[0].get_text(strip=True).find('(')+1
        end = attribute.find_all('span')[0].get_text(strip=True).find(')')
        row['date_created'] = attribute.find_all('span')[0].get_text(strip=True)[start:end].replace('\'','20')
        try:
            row['last_upvoted'] = attribute.find_all('span',{'class':'sLastComment'})[0].get_text(strip=True)[9:]
        except:
            pass
        row['comments'] = attribute.find_all('span',{'class':'sLabel'})[0].get_text(strip=True)[10:]
        try:
            row['status'] = attribute.find_all('div',{'class':'sLabels'})[0].get_text(strip=True).replace('Pinned','')
        except:
            pass
        link = attribute.find('a')['href']
        row['suggestion_link'] = f'https://feedback.mutual.app{link}'
        rows.append(row)

    # List of dict: 'votes' attribute
    votes= soup.find_all('div',{'class':'sNumbers'})
    for attribute in votes:
        row = {}
        row['votes'] = attribute.find('a').get_text(strip=True)[:-5].replace('K','000')
        rows_votes.append(row)

    
    # if there is not a next page, stop loop
    page+=1
    if soup.find_all('li')[-1].find('a') == None:
        page = False

rows_merged = []
# Merge both list of dict into new list
for idx, row in enumerate(rows):
    rows_merged.append({**row,**rows_votes[idx]})

# build dataframe
data = pd.DataFrame(rows_merged)

# change dtype
data = data.astype({'votes': 'float','comments': 'float'}, copy=True)
# add column with months
data['date_created_month'] = data['date_created'].apply(
    lambda x:
    x.split(' ')[1].replace(',','')
    if 'days' not in x
    else datetime.now().strftime('%h'))

# find logo
url = 'https://blog.mutual.app/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
logo = soup.find('img')['src']

# ----------------------------------- scripts 1 -----------------------------------

data_month = data['date_created_month'].value_counts().reset_index()
order = {'index':['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']}

fig = px.bar(
    data_month,
    x='index',
    y='date_created_month',
    color='date_created_month',
    # color_continuous_scale=px.colors.sequential.Viridis,
    color_continuous_scale=str(px.colors.named_colorscales()[15])+'_r',
    category_orders=order,
    width=1200,
    height=400,
    text_auto=True,
    labels={"index":"Month","date_created_month":"Amount of Feedback"},
    title="Feedback per Month")

fig.update_traces(textfont_size=15)

fig_1 = fig

# ----------------------------------- scripts 1 -----------------------------------

script_1 = '''
url_base = 'feedback.mutual.app'

page = 1 # used later for loop over all pages

url = f'https://{url_base}/?page={page}&order=popular&filter=all#controls' # url for each page. only change the page number

response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

info = soup.find_all('div',{'class':'sInfo'})

rows = []

for attribute in info:
    row = {}
    row['page'] = page
    row['id'] = attribute.find('a')['href'].split('/')[2]
    row['suggestion'] = attribute.find('a')['href'].split('/')[-1].replace('-',' ').capitalize()
    row['author'] = attribute.find_all('strong')[0].get_text()
    start = attribute.find_all('span')[0].get_text(strip=True).find('(')+1
    end = attribute.find_all('span')[0].get_text(strip=True).find(')')
    row['date_created'] = attribute.find_all('span')[0].get_text(strip=True)[start:end].replace('\'','20')
    row['last_upvoted'] = attribute.find_all('span',{'class':'sLastComment'})[0].get_text(strip=True)[9:]
    row['comments'] = attribute.find_all('span',{'class':'sLabel'})[0].get_text(strip=True)[10:]
    row['status'] = attribute.find_all('div',{'class':'sLabels'})[0].get_text(strip=True).replace('Pinned','')
    rows.append(row)
'''
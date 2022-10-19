
import requests # to get the html markdown from the url
from bs4 import BeautifulSoup # to make the html readable
import pandas as pd # to save table in a csv

# Get the data from website
url = 'https://web.byui.edu/SurplusList/'
html_data = requests.get(url)
soup = BeautifulSoup(html_data.text, 'html.parser')

# Build Table
rows=[]
for item in soup.find_all('tr')[13:]:
    row={}
    row['Item Number'] = item.select('td')[0].text
    row['Qty'] = item.select('td')[1].text
    row['Description'] = item.select('td')[2].text
    row['Condition'] = item.select('td')[3].text
    row['Price'] = item.select('td')[4].text
    row['Location'] = item.select('td')[5].text
    row['Quick/Bid'] = item.select('td')[6].text
    row['Image'] = item.select('td')[7].text
    rows.append(row)

data = pd.DataFrame(rows)

data.drop(data.tail(1).index,inplace=True) # Drop last row (is empty)

# ------------- plots -------------

import matplotlib.pyplot as plt
import plotly.express as px


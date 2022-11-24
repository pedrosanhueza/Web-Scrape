
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

# Change column data types
data.Price = pd.to_numeric(data.Price.str.replace("$","",regex=True).replace(",","",regex=True))
data['Item Number'] = pd.to_numeric(data['Item Number'])

# data.Qty = pd.to_numeric(data.Qty)
data.Qty = data.Qty.apply(lambda x: int(x))
data.Condition = data.Condition.str.capitalize()
a = data.copy()

# -------------------------- PLOT 1
data_1 = data.reindex(data.index.repeat(data.Qty)).reset_index().drop(['index','Qty'], axis=1) # repeat rows based on quantity
# data_1_names = data_1['Condition'].value_counts().reset_index()['index']
# data_1_values = data_1['Condition'].value_counts().reset_index()['Condition']



# Simple Web Scrape and EDA

# __Website:__ [www.CountryCode.org]("https://countrycode.org/") <br />
# __Data Composition:__ Country Name, Country Telephone Code, ISO Code, Population Amount, Area km2, GDP in USD <br />
# __Running Time:__ 3.1 sec <br />
# __Project:__ Non-commercial use <br /><br />
# __Author:__ Pedro Sanhueza

# In[0]:

### Import libraries
import requests # get html from URL
from bs4 import BeautifulSoup # find elements in html
import pandas as pd # build data frame
import plotly.express as px # display plots
from datetime import datetime # to save file with current time

# In[1]:

### Webscrape URL
response = requests.get("https://countrycode.org/") # read data from URL

soup = BeautifulSoup(response.text, 'html.parser') # convert web data to HTML

ls = [x.get_text() for x in soup.select('td')][:240*6] # collect all values of table into a list

# In[2]:

### Build Data Table
data = { # get the 6th item in list starting from 1, 2, 3, 4, 5, and 6th element
'Country' :ls[0::6],
'Country_code' : ls[1::6],
'ISO_codes' : ls[2::6],
'Population' : ls[3::6],
'Area_KM2' : ls[4::6],
'GDP_USD' : ls[5::6]
}

df = pd.DataFrame(data) # build data frame

df # showcase the extraction of the website table

# In[3]:

### GDP per country plot

def gdp_value(x): # from str to int
    try:
        y = str(x).split(' ') # divide string in two
        z  = float(y[0]) * float(y[1]) # multiply the original value with the replacement amount
        return int(z) # return the integer of the multiplication
    except:
        return "No Value Found"

replacements = {'Billion':'1000000000', 'Million':'1000000', 'Trillion': '1000000000000'} # key items to be replaced

df['GDP_USD'] = [ gdp_value(x) for x in df.GDP_USD.replace(replacements, regex=True)] # change from strings to integers

df1 = df[(df['GDP_USD'] != "No Value Found")].sort_values(by=['GDP_USD'] )[-10:].copy() # get the top 10 in order

px.bar(df1, x='Country', y='GDP_USD',  title="GDP per Country", text_auto=True) # display bar chart

# In[4]:

### Population per country plot
df['Population'] = [ int(x) for x in df.Population.replace(',','', regex=True)] # change from strings to integers

df2 = df.sort_values(by=['Population'], ascending=False)[:10].copy() # get the top 10 in order

px.bar(df2, x='Country', y='Population', title="Top 10 Countries Population Count", text_auto=True, color='Population') # display bar chart

# In[5]:

### Population vs Area plot
df['Area_KM2'] = [int(x) for x in df.Area_KM2.replace(',','', regex=True)] # change from strings to integers

fig = px.scatter(df, x="Area_KM2", y="Population", color='Area_KM2', text='Country', title="Area vs Population Amount") # build scatter plot

fig.update_traces(textposition='top center') # display plot

# In[6]:

### Save Table
# optional:

file_path = '../Country Code - Historical Data/Country Code ' + datetime.now().strftime("%d-%m-%Y %H%M%S") + ".csv" # folder location with file name

df.to_csv(file_path) # save data frame as csv in file location

import requests # to download html source from url
from bs4 import BeautifulSoup # find elements in html
import pandas as pd # build dataframe

### Webscrape URL

url = "https://countrycode.org/"
response = requests.get(url) # download html source from url
soup = BeautifulSoup(response.text, 'html.parser') # make html data readable for BeautifulSoup

ls = [x.get_text() for x in soup.select('td')][:240*6] # collect all values of table into a list

### Build Data Table
json_list = { # get the 6th item in list starting from 1, 2, 3, 4, 5, and 6th element
'Country'      :ls[0::6],
'Country_code' : ls[1::6],
'ISO_codes'    : ls[2::6],
'Population'   : ls[3::6],
'Area_KM2'     : ls[4::6],
'GDP_USD'      : ls[5::6]}

data = pd.DataFrame(json_list) # build data frame

# ------------------------------ FIRST PLOT ------------------------------

def gdp_value(x): # from str to int -- Change 'GDP_USD' column integers
    try:
        y = str(x).split(' ') # divide string in two
        z  = float(y[0]) * float(y[1]) # multiply the original value with the replacement amount
        return int(z) # return the integer of the multiplication
    except:
        return "No Value Found"
replacements = {'Billion':'1000000000', 'Million':'1000000', 'Trillion': '1000000000000'} # key items to be replaced
data['GDP_USD'] = [ gdp_value(x) for x in data.GDP_USD.replace(replacements, regex=True)] # change from strings to integers
df1 = data[(data['GDP_USD'] != "No Value Found")].sort_values(by=['GDP_USD'] )[-10:].copy() # get the top 10 in order

# ------------------------------ SECOND PLOT ------------------------------

data['Population'] = [ int(x) for x in data.Population.replace(',','', regex=True)] # change from strings to integers
df2 = data.sort_values(by=['Population'], ascending=False)[:10].copy() # get the top 10 in order

# ------------------------------ THIRD PLOT ------------------------------

data['Area_KM2'] = [int(x) for x in data.Area_KM2.replace(',','', regex=True)] # change from strings to integers
data['Population'] = [int(x) for x in data.Population.replace(',','', regex=True)]
# --------------------------------------------
script_1 = '''
import requests # to download html source from url
from bs4 import BeautifulSoup # find elements in html
import pandas as pd # build data frame

### Webscrape URL

url = "https://countrycode.org/"
response = requests.get(url) # download html source from url
soup = BeautifulSoup(response.text, 'html.parser') # make html data readable for BeautifulSoup

ls = [x.get_text() for x in soup.select('td')][:240*6] # collect all values of table into a list

### Build Data Table
json_list = { # get the 6th item in list starting from 1, 2, 3, 4, 5, and 6th element
'Country' :ls[0::6],
'Country_code' : ls[1::6],
'ISO_codes' : ls[2::6],
'Population' : ls[3::6],
'Area_KM2' : ls[4::6],
'GDP_USD' : ls[5::6]}

data = pd.DataFrame(json_list) # build data frame

data.to_csv('Country_Codes.csv', index=False)
'''
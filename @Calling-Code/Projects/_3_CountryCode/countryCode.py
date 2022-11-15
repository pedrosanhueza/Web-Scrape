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
'''
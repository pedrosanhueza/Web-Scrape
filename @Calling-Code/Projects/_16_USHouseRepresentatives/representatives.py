import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.house.gov/representatives"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

tables = soup.select('table')

rows = []
for table in tables[:56]:
    row = {}
    row['District']             = [x.text.strip() for x in table.select('td')][0::6]
    row['Name']                 = [x.text.strip() for x in table.select('td')][1::6]
    row['Party']                = [x.text.strip() for x in table.select('td')][2::6]
    row['Office Room']          = [x.text.strip() for x in table.select('td')][3::6]
    row['Phone']                = [x.text.strip() for x in table.select('td')][4::6]
    row['Committee Assignment'] = [x.text.strip() for x in table.select('td')][5::6]
    row['State']                = table.select_one('caption').text.strip()
    rows.append(pd.DataFrame(row))
a = row
# data = pd.concat(rows)

# ---------------------------------------

script1 = '''
import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.house.gov/representatives"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

tables = soup.select('table')

rows = []
for table in tables[:56]:
    row = {}
    row['District']             = [x.text.strip() for x in table.select('td')][0::6]
    row['Name']                 = [x.text.strip() for x in table.select('td')][1::6]
    row['Party']                = [x.text.strip() for x in table.select('td')][2::6]
    row['Office Room']          = [x.text.strip() for x in table.select('td')][3::6]
    row['Phone']                = [x.text.strip() for x in table.select('td')][4::6]
    row['Committee Assignment'] = [x.text.strip() for x in table.select('td')][5::6]
    row['State']                = table.select_one('caption').text.strip()
    rows.append(pd.DataFrame(row))

data = pd.concat(rows)
'''
import requests
from bs4 import BeautifulSoup
import pandas as pd
import random

url = "https://www.house.gov/representatives"

user_agents = [
  "Mozilla/5.0 (Windows NT 10.0; rv:91.0) Gecko/20100101 Firefox/91.0",
  "Mozilla/5.0 (Windows NT 10.0; rv:78.0) Gecko/20100101 Firefox/78.0",
  "Mozilla/5.0 (X11; Linux x86_64; rv:95.0) Gecko/20100101 Firefox/95.0",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36"
]

random_user_agent = random.choice(user_agents)

# headers = {'User-Agent': random_user_agent}

headers = {
    'cookie': "ASP.NET_SessionId=5qcvlysfw5tmg1t1xb0kdtvo; __cf_bm=fyaOzWIZIjxrw.x1g.M5csBYMVeWnKc.6yR9rFTakHc-1669404095-0-AZjkuXVCL/D4Tyof/I0EDexjPn4sA/vXA8XcyNKcKyN2G8qa/n8bKQ34+UTNKwndus0wWOvmB4mBDdhQLN9vxYDNnDIi8sDIXO6rL4oCFe/hGEM2SRyHlinfQmKCtH/HaRgBlwAA5rxodyDALWOrKpk=",
    'authority': "sosbiz.idaho.gov",
    # 'accept': "*/*",
    # 'accept-language': "en-US,en;q=0.5",
    # 'authorization': "undefined",
    # 'content-type': "application/json",
    # 'origin': "https://sosbiz.idaho.gov",
    # 'referer': "https://sosbiz.idaho.gov/search/business",
    # 'sec-ch-ua': '"Chromium";v="106", "Brave Browser";v="106", "Not;A=Brand";v="99"',
    # 'sec-ch-ua-mobile': "?0",
    # 'sec-ch-ua-platform': '"macOS"',
    # 'sec-fetch-dest': "empty",
    # 'sec-fetch-mode': "cors",
    # 'sec-fetch-site': "same-origin",
    # 'sec-gpc': "1",
    'user-agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36"
    }

response = requests.get(url, headers=headers)

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
    df_state = pd.DataFrame(row)
    rows.append(df_state)

# data = pd.Series([1,2,3,4])
# data = rows[0]
# data = pd.concat([rows[0],rows[1]])
data = pd.concat(rows)

# ---------------------------------------

script_1 = ''' 
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
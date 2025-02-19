import requests
from bs4 import BeautifulSoup
import pandas as pd 
from datetime import datetime

url = 'https://www.foxsports.com/soccer/2022-fifa-world-cup/teams'

script_1 = '''
import requests
from bs4 import BeautifulSoup
import pandas as pd 
from datetime import datetime

url = 'https://www.foxsports.com/soccer/2022-fifa-world-cup/teams'
response = requests.get(url)
soup = BeautifulSoup(response.text, features="html.parser")
country_name = [x.text for x in soup.find_all('h3')]
countries = [x['href'] for x in soup.find_all('a',{'class':'entity-list-row-container image-logo'})]

# ---------------------------------------- running time: 1m 20s ---------------------------------------- #

title = ['GOALKEEPER', 'POS', 'AGE', 'HT', 'WT']

rows=[]

for idx,country in enumerate(countries):

    url_root = f'https://www.foxsports.com{country}-roster'
    soup = BeautifulSoup(requests.get(url_root).text, 'html.parser')

    table = soup.find('div',{'view':'team'})
    # title = [x.text.strip() for x in table.find('tr')]
    # title = [x.text.strip() for x in table.find_all('tr')[0]]
    try:
        for group in table.find_all('tbody')[:-1]:
            for player in group:
                row={}
                row['Country'] = country_name[idx].capitalize()
                row['Name'] = player.find('h3').text
                row[title[1]] = player.find('td',{'data-index':'1'}).text.strip()
                row[title[2]] = player.find('td',{'data-index':'2'}).text.strip()
                row[title[3]] = player.find('td',{'data-index':'3'}).text.strip()
                row[title[4]] = player.find('td',{'data-index':'4'}).text.strip()
                row['Country_logo'] = soup.find('source')['srcset']
                rows.append(row)
    except:
        pass

data = pd.DataFrame(rows)

data = data[~data.isin(['-']).any(axis=1)] # drop rows with missing data

POS_mapped = {'G': 'Goalkeeper', 'D': 'Defender', 'M': 'Midfielder', 'F': 'Forward'}

data.replace({title[1]: POS_mapped}, inplace=True) # "POS" is hard coded. Check when debugging

# age column to number
data[title[2]] = pd.to_numeric(data[title[2]])

# inches to centimeters
data[title[3]] = data[title[3]].apply(lambda x: (int(x.split('\'')[0])*12 + int(x.split('\'')[1].replace('\"',''))) * 2.54)

# weight column to number
data[title[4]] = data[title[4]].apply(lambda x: round(int(x.split(' ')[0]) / 2.205,1)) # lbs to kg

# add BMI column
data['BMI'] = data.apply(lambda x: round(x.WT / (x.HT/100)**2,1) , axis=1)
'''

data = pd.read_csv("@Calling-Code/Projects/_4_FIFAWorldCup/2022-fifa-world-cup.csv")

# ---------------------------------------------------------------- DATA EXTRACTION ---------------------------------------------------------------- #

def data_extraction():
    headers = {'user-agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36"}
    response = requests.get(url,headers=headers)
    soup = BeautifulSoup(response.text, features="html.parser")
    country_name = [x.text for x in soup.find_all('h3')]
    countries = [x['href'] for x in soup.find_all('a',{'class':'entity-list-row-container image-logo'})]

    # ---------------------------------------- running time: 1m 20s ---------------------------------------- #

    title = ['GOALKEEPER', 'POS', 'AGE', 'HT', 'WT']

    rows=[]

    for idx,country in enumerate(countries):

        url_root = f'https://www.foxsports.com{country}-roster'
        soup = BeautifulSoup(requests.get(url_root).text, 'html.parser')

        table = soup.find('div',{'view':'team'})
        # title = [x.text.strip() for x in table.find('tr')]
        # title = [x.text.strip() for x in table.find_all('tr')[0]]
        try:
            for group in table.find_all('tbody')[:-1]:
                for player in group:
                    row={}
                    row['Country'] = country_name[idx].capitalize()
                    row['Name'] = player.find('h3').text
                    row[title[1]] = player.find('td',{'data-index':'1'}).text.strip()
                    row[title[2]] = player.find('td',{'data-index':'2'}).text.strip()
                    row[title[3]] = player.find('td',{'data-index':'3'}).text.strip()
                    row[title[4]] = player.find('td',{'data-index':'4'}).text.strip()
                    row['Country_logo'] = soup.find('source')['srcset']
                    rows.append(row)
        except:
            pass

    data = pd.DataFrame(rows)

    data = data[~data.isin(['-']).any(axis=1)] # drop rows with missing data

    POS_mapped = {'G': 'Goalkeeper', 'D': 'Defender', 'M': 'Midfielder', 'F': 'Forward'}

    title = ['GOALKEEPER', 'POS', 'AGE', 'HT', 'WT']

    data.replace({title[1]: POS_mapped}, inplace=True) # "POS" is hard coded. Check when debugging

    try:
        # age column to number
        data[title[2]] = pd.to_numeric(data[title[2]])

        # inches to centimeters
        data[title[3]] = data[title[3]].apply(lambda x: (int(x.split('\'')[0])*12 + int(x.split('\'')[1].replace('\"',''))) * 2.54)

        # weight column to number
        data[title[4]] = data[title[4]].apply(lambda x: round(int(x.split(' ')[0]) / 2.205,1)) # lbs to kg
        
        # add BMI column
        data['BMI'] = data.apply(lambda x: round(x.WT / (x.HT/100)**2,1) , axis=1)
    except:
        pass

    return data


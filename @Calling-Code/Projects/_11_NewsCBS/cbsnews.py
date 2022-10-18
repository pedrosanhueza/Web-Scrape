import requests
from bs4 import BeautifulSoup
import pandas as pd 

url = 'https://www.cbsnews.com/world/'

response = requests.get(url)

soup = BeautifulSoup(response.text)

rows = [] # list of information for each article

sections = soup.find_all('section')

for section in sections:

    articles = section.find_all('article')
    
    try:
        # print(section.find('h3').text.strip())
        for article in articles:
            row = {}
            row['Section'] = section.find('h3').text.strip()
            row['Title'] = article.find('h4').text.strip()
            row['Description'] = article.find('p').text.strip()
            row['Date'] = article.find('li').text
            row['url_article'] = article.find('a')['href']
            row['url_image'] = article.find('img')['src']
            rows.append(row)
    except:
        pass

data = pd.DataFrame(rows)
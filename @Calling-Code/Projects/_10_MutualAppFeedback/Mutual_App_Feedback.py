import requests
from bs4 import BeautifulSoup
import pandas as pd

data = pd.DataFrame({'A':range(10)})

# # running time: 7 minutes
# rows_info = []
# rows_votes = []
# rows_description=[]

# for pag in range(7): # '7' because there are 7 pages
#     url = f'https://feedback.mutual.app/?page={pag+1}&order=popular&filter=all#controls' # url for each page. only change the page number
#     response = requests.get(url)
#     soup = BeautifulSoup(response.text, 'html.parser')

#     info = soup.find_all('div',{'class':'sInfo'})
#     votes= soup.find_all('div',{'class':'sNumbers'})

#     #************* INFO DICTIONARARY *************
#     for attribute in info:
#         row = {}
#         row['id'] = attribute.find('a')['href'].split('/')[2]
#         row['suggestion'] = attribute.find('a')['href'].split('/')[-1].replace('-',' ').capitalize()
#         row['author'] = attribute.find_all('strong')[0].get_text()

#         start = attribute.find_all('span')[0].get_text(strip=True).find('(')+1
#         end = attribute.find_all('span')[0].get_text(strip=True).find(')')
        
#         row['date_created'] = attribute.find_all('span')[0].get_text(strip=True)[start:end].replace('\'','20')
#         row['last_upvoted'] = attribute.find_all('span',{'class':'sLastComment'})[0].get_text(strip=True)[9:].replace('\'','20')
#         row['comments'] = attribute.find_all('span',{'class':'sLabel'})[0].get_text(strip=True)[10:]
#         try:
#             row['status'] = attribute.find_all('div',{'class':'sLabels'})[0].get_text(strip=True).replace('Pinned','')
#         except:
#             pass
#             # pass 
#         rows_info.append(row)

#     #************* VOTES DICTIONARARY *************
#     for attribute in votes:
#         row = {}
#         row['votes'] = attribute.find('a').get_text(strip=True)[:-5].replace('K','000')
#         rows_votes.append(row)

#     # ************* DESCRIPTION DICTIONARARY *************
#     for attribute in info:
#         url = f'https://feedback.mutual.app'+attribute.find('a')['href']
#         response = requests.get(url)
#         soup = BeautifulSoup(response.text, 'html.parser')
#         row = {}
#         p = soup.find('div',{'class':'suggestionDescription'}).get_text().strip()
#         row['Description'] = p.encode('ascii','replace').decode().replace('???','\'')
#         rows_description.append(row)


#     #************* JOIN *************
#     for idx,e in enumerate(rows_votes):
#         rows_info[idx].update(e)

#     for idx,e in enumerate(rows_description):
#         rows_info[idx].update(e)

# data = pd.DataFrame(rows_info)
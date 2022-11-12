import requests # to get the html markdown from the url
from bs4 import BeautifulSoup # to make the html readable
import pandas as pd # to save table in a csv

url_main = 'https://sinca.mma.gob.cl/'

# List of all IG urls
url = 'https://sinca.mma.gob.cl/'
html_data = requests.get(url)
soup = BeautifulSoup(html_data.text, 'html.parser')

# list of all regions link. Each region page has their stations link. From station link we get the data.
regiones = ['https://sinca.mma.gob.cl/'+x['href'] for x in soup.findAll('a')][15:-4]

# running time: 32s
# get list of urls. all station links
url_stations = []
for page in regiones:
    html_data = requests.get(page)
    soup = BeautifulSoup(html_data.text, 'html.parser')
    url_stations = url_stations + [x.findAll('a')[0]['href'] for x in soup.find_all('tbody')[0].find_all('tr')]
# running time 3m 30s

rows=[]
for region in url_stations:
    url = 'https://sinca.mma.gob.cl'+region
    html_data = requests.get(url)
    soup = BeautifulSoup(html_data.text, 'html.parser')
    estacion = soup.select('h1')[1].text.split(' ')[1:]
    estacion = ' '.join(estacion)
    GI_cols =   [ x.get_text().strip() for x in soup.find_all('th',{'class':'right'})]
    GI_values = [ x.get_text().strip() for x in soup.find_all('td',{'class':'left'}) ]
    row={}

    for idx in range(len(GI_values)):
        row.update({GI_cols[idx] : GI_values[idx]})
    row.update({'Estacion_id':int(region.split('/')[-1])})
    row.update({'Estacion':estacion})
    row.update({'URL':url})
    rows.append(row)

data = pd.DataFrame(rows)

data['Región'] = data['Región'].apply(lambda x: x.replace('de ',''))

# data['Huso horario'] = data['Huso horario'].apply(lambda x: int(x))

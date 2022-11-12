import requests
from bs4 import BeautifulSoup
import pandas as pd 

url_main = 'https://www.camara.cl/diputados/diputados.aspx#mostrarDiputados'

url = 'https://www.camara.cl/diputados/diputados.aspx#mostrarDiputados'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

profiles_uls = [x.find('a')['href'] for x in soup.find_all('article',{'class':'grid-2'})] # lista de url perfiles

# ------------ SIMPLE TABLE ------------
# running time: 3 min 2s
diputados = []
for diputado in soup.find_all('article',{'class':'grid-2'}):
    row = {}
    row['ID'] = diputado.find('a')['href'].split('=')[-1]
    row['Name'] = diputado.find('h4').text
    row['Distrito'] = diputado.find('p').text
    row['Partido'] = diputado.find_all('p')[-1].text
    row['website'] = 'https://www.camara.cl/diputados/' + diputado.find('a')['href']
    row['img'] = 'https://www.camara.cl' + diputado.find('img')['src']
    diputados.append(row)
data_simple = pd.DataFrame(diputados)

# ------------ COMPLETE TABLE ------------
# running time: 3 min 2s
rows=[]
for profile in profiles_uls:
    url = 'https://www.camara.cl/diputados/' + profile
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    row={}
    row['Nombre'] = soup.find('h2').text[9:]
    row['Periodos parlamentarios'] = str([x.text for x in soup.find_all('div',{'class':'grid-2 aleft m-left14'})[2].find_all('li')[1:]]).replace('\'','')[1:-1]
    row['Comunas'] =        soup.find_all('p')[2].text.split('\n')[1].split(':')[1].strip()
    row['Distrito'] =       soup.find_all('p')[2].text.split('\n')[2].split(':')[1].strip().replace('Nº ','')
    row['Región'] =         soup.find_all('p')[2].text.split('\n')[3].split(':')[1].strip()
    row['Período Actual'] = soup.find_all('p')[2].text.split('\n')[4].split(':')[1].strip()
    row['Partido'] =        soup.find_all('p')[2].text.split('\n')[5].split(':')[1].strip()
    row['Bancada'] =        soup.find_all('p')[2].text.split('\n')[6].split(':')[1].strip()
    row['Email'] =          soup.find('i',{'class':'fa fa-envelope-o'}).parent.text.split('\n')[-1].split()[0]
    rows.append(row)
data = pd.DataFrame(rows)
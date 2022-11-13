
import requests
import pandas as pd

url_main = 'https://www.boattrader.com/boat-dealers/'

url = 'https://api.boattrader.com/app/boat-dealers/dealers'

parameters = {'apikey': '8b08b9bc353c494a80c60fb86debfc56','pageSize': 3000,'page': 1}

response = requests.get(url, params=parameters)

json_list = response.json()['records']

df = pd.DataFrame(json_list)

columns = [
    'id',
    # 'parentId',
    'name',
    'displayName',
    'email',
    'street',
    'city',
    'countrySubDivisionCode',
    'postalCode',
    # 'country',
    'phone',
    'website',
    # 'logoPath',
    # 'logoUrl',
    'coordinates'
]

df_final = df[columns].rename(columns={"displayName": "title",'countrySubDivisionCode':'state'})

df_final['lat']  = df_final.coordinates.apply(lambda x : x[0] if type(x) == list else x)
df_final['long'] = df_final.coordinates.apply(lambda x : x[1] if type(x) == list else x)

df_final.drop('coordinates', axis=1, inplace=True)

data = df_final

# ----------------------------------------------------------------

script_1 = '''

import requests
import pandas as pd

url_main = 'https://www.boattrader.com/boat-dealers/'

url = 'https://api.boattrader.com/app/boat-dealers/dealers'

parameters = {'apikey': '8b08b9bc353c494a80c60fb86debfc56','pageSize': 3000,'page': 1}

response = requests.get(url, params=parameters)

json_list = response.json()['records']

df = pd.DataFrame(json_list)

columns = [
    'id',
    # 'parentId',
    'name',
    'displayName',
    'email',
    'street',
    'city',
    'countrySubDivisionCode',
    'postalCode',
    # 'country',
    'phone',
    'website',
    # 'logoPath',
    # 'logoUrl',
    'coordinates'
]

df_final = df[columns].rename(columns={"displayName": "title",'countrySubDivisionCode':'state'})

df_final['lat']  = df_final.coordinates.apply(lambda x : x[0] if type(x) == list else x)
df_final['long'] = df_final.coordinates.apply(lambda x : x[1] if type(x) == list else x)

df_final.drop('coordinates', axis=1, inplace=True)

data = df_final

'''
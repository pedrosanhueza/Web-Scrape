import requests
import pandas as pd
from bs4 import BeautifulSoup

url = "https://www.forbes.com/billionaires/page-data/index/page-data.json"

response = requests.get(url)

json_data = response.json()

rows = json_data['result']['pageContext']['tableData']

ls_=[]

for row in rows:
    tableData = {
        k: v
        for (k, v) in row.items()
        if
        (k != 'person') & # dict
        (k != 'employment') & # dict
        (k != 'qas') & # two dicts
        (k != 'bios') & # list
        (k != 'abouts') & #list
        (k != 'csfDisplayFields') #list
        }
    ls_.append(tableData)

# data = pd.DataFrame(ls_)

data = pd.DataFrame([tableData])

# cols_to_drop = [
#     'parentListUri',
#     'organization',
#     'title',
#     'selfMadeRank',
#     'residenceStateRegion',
#     'embargo',
#     'residenceMsa',
#     'impactInvestor',
#     'numberOfSiblings',
#     'numberOfSiblingsEst',
#     'bio',
#     # 'totalCharitableDonation',
#     # 'charitableDonationPercentage',
#     'thumbnail',
#     'notableDeal',
#     'valueCreated',
#     'primaryIndustry',
#     'portraitImage',
#     'landscapeImage',
#     'clients']

# data.drop(cols_to_drop, axis=1, inplace=True)

# data['squareImage'].fillna('https://i.forbesimg.com/media/assets/forbes_1200x1200.jpg', inplace=True)

# data['country'].fillna('Not Specified', inplace=True)

# data['state'].fillna('Not Specified', inplace=True)

# data['city'].fillna('Not Specified', inplace=True)

# data['gender'].fillna('Not Specified', inplace=True)

# data['birthDate'].fillna('Not Specified', inplace=True)

# data['firstName'].fillna('Not Specified', inplace=True)

# data = pd.DataFrame(range(20))

# --------------------------------------------------------------------

script = """
import requests
import pandas as pd
from bs4 import BeautifulSoup

url = "https://www.forbes.com/billionaires/page-data/index/page-data.json"

response = requests.get(url)

json_data = response.json()

rows = json_data['result']['pageContext']['tableData']

tableData = {
    k: v
    for (k, v) in rows[0].items()
    if
    (k != 'person') & # dict
    (k != 'employment') & # dict
    (k != 'qas') & # two dicts
    (k != 'bios') & # list
    (k != 'abouts') & #list
    (k != 'csfDisplayFields') #list
}

ls_=[]

for row in rows:
    tableData = {
        k: v
        for (k, v) in row.items()
        if
        (k != 'person') & # dict
        (k != 'employment') & # dict
        (k != 'qas') & # two dicts
        (k != 'bios') & # list
        (k != 'abouts') & #list
        (k != 'csfDisplayFields') #list
        }
    ls_.append(tableData)

data = pd.DataFrame(ls_)

cols_to_drop = [
    'parentListUri',
    'organization',
    'title',
    'selfMadeRank',
    'residenceStateRegion',
    'embargo',
    'residenceMsa',
    'impactInvestor',
    'numberOfSiblings',
    'numberOfSiblingsEst',
    'bio',
    # 'totalCharitableDonation',
    # 'charitableDonationPercentage',
    'thumbnail',
    'notableDeal',
    'valueCreated',
    'primaryIndustry',
    'portraitImage',
    'landscapeImage',
    'clients']

data.drop(cols_to_drop, axis=1, inplace=True)

data['squareImage'].fillna('https://i.forbesimg.com/media/assets/forbes_1200x1200.jpg', inplace=True)

data['country'].fillna('Not Specified', inplace=True)

data['state'].fillna('Not Specified', inplace=True)

data['city'].fillna('Not Specified', inplace=True)

data['gender'].fillna('Not Specified', inplace=True)

data['birthDate'].fillna('Not Specified', inplace=True)

data['firstName'].fillna('Not Specified', inplace=True)

"""
import requests
from bs4 import BeautifulSoup
import pandas as pd

url_main = "https://apps.shopify.com/"

title = []
href = []
developer = []
details = []
review_count = []
icon_logo = []
pricing = []

for page in range(1,201): # first 200 pages (sort by most relevant)
    url = f"https://apps.shopify.com/browse?page={page}"
    response = requests.get(url)
    
    soup = BeautifulSoup(response.text)
    [ title.append(x['title']) for x in soup.find_all('div',{'class','ui-app-card'}) ]
    [ href.append(x['data-target-href']) for x in soup.find_all('div',{'class','ui-app-card'}) ]
    [ developer.append(x.text) for x in soup.find_all('div',{'class':'ui-app-card__developer-name'}) ]
    [ details.append(x.text) for x in soup.find_all('p',{'class':'ui-app-card__details'}) ]
    [ review_count.append(x.text) for x in soup.find_all('span',{'class':'ui-review-count-summary'}) ]
    [ icon_logo.append(x['src']) for x in soup.find_all('img',{'class':'ui-app-card__icon'}) ]
    [ pricing.append(x.text) for x in soup.find_all('div',{'class':'ui-app-card__pricing'}) ]

data = pd.DataFrame({
    'name': title,
    'url': href,
    'developer': developer,
    'details': details,
    'review_count': review_count,
    'icon_logo': icon_logo,
    'pricing': pricing
})

data.name = data.name.str.replace("Go to ","",regex=True)
data.name = data.name.str.replace(f'{chr(8209)}',"",regex=True)
data.developer = data.developer.str.replace("by ","",regex=True)
data.review_count = data.review_count.str.replace("(","",regex=True)
data.review_count = data.review_count.str.replace(")","",regex=True)
data.review_count = data.review_count.str.replace("reviews","",regex=True)
data.pricing = data.pricing.str.replace('Free to install','Free', regex=True)
data.pricing = data.pricing.str.replace('Free plan available','Free', regex=True)

#  -------------------- script_1 ---------------------------------------------------- #

script_1 = '''
import requests
from bs4 import BeautifulSoup
import pandas as pd

title = []
href = []
developer = []
details = []
review_count = []
icon_logo = []
pricing = []

for page in range(1,201): # first 200 pages (sort by most relevant)
    url = f"https://apps.shopify.com/browse?page={page}"
    response = requests.get(url)
    
    soup = BeautifulSoup(response.text)
    [ title.append(x['title']) for x in soup.find_all('div',{'class','ui-app-card'}) ]
    [ href.append(x['data-target-href']) for x in soup.find_all('div',{'class','ui-app-card'}) ]
    [ developer.append(x.text) for x in soup.find_all('div',{'class':'ui-app-card__developer-name'}) ]
    [ details.append(x.text) for x in soup.find_all('p',{'class':'ui-app-card__details'}) ]
    [ review_count.append(x.text) for x in soup.find_all('span',{'class':'ui-review-count-summary'}) ]
    [ icon_logo.append(x['src']) for x in soup.find_all('img',{'class':'ui-app-card__icon'}) ]
    [ pricing.append(x.text) for x in soup.find_all('div',{'class':'ui-app-card__pricing'}) ]

data = pd.DataFrame({
    'name': title,
    'url': href,
    'developer': developer,
    'details': details,
    'review_count': review_count,
    'icon_logo': icon_logo,
    'pricing': pricing
})

data.name = data.name.str.replace("Go to ","",regex=True)
data.name = data.name.str.replace(f'{chr(8209)}',"",regex=True)
data.developer = data.developer.str.replace("by ","",regex=True)
data.review_count = data.review_count.str.replace("(","",regex=True)
data.review_count = data.review_count.str.replace(")","",regex=True)
data.review_count = data.review_count.str.replace("reviews","",regex=True)
data.pricing = data.pricing.str.replace('Free to install','Free', regex=True)
data.pricing = data.pricing.str.replace('Free plan available','Free', regex=True)
'''
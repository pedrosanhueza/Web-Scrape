
## ----------------------------------------- Import -------------------------------------------------------------------------------------- ##
import streamlit as st
import pandas as pd

# from Projects import SurplusStore      #1
from Projects.CatalogBYUI import catalogBYUI       #2
from Projects import countryCode   #3
from Projects import FIFAWorldCup    #4
# from Projects import SurplusStore    #5
# from Projects import SurplusStore    #6
# from Projects import SurplusStore    #7
# from Projects import SurplusStore    #8
# from Projects import SurplusStore    #9
# from Projects import SurplusStore    #10
# from Projects import SurplusStore    #11
# from Projects import SurplusStore    #12
# from Projects import SurplusStore    #13
# from Projects import SurplusStore    #14
from Projects import SurplusStore    #15
from Projects import representatives    #16
# from Projects import SurplusStore    #17


st.write('# Web Analysis')
st.write('''
    __Author__ : Pedro Sanhueza \n
    Description: Web Scraping EDA
    ''')

## ----------------------------------------- Beggin Side Bar ----------------------------------------------------------------------------- ##

options = (
   'Billionaires',
   'Class Catalog - BYUI',
   'Country Code',
   'FIFA World Cup',
   'Financial Data',
   'Forbes - Billionaries',
   'Forbes - Universities',
   'Irvine Spectrum Center',
   'Job Board - BYUI',
   'Mutual App Feedback',
   'News - CBS',
   'Politicos Chilenos',
   'Políticos Españoles',
   'SINCA MMA Gob',
   'Surplus Store - BYUI',
   'US House of Representatives',
   'test')

option = st.sidebar.selectbox('Web Scraping Projects', options)

## ----------------------------------------- Modules Variables ------------------------------------------------------------------------ ##
## data
## url - scrape
## url - website

projectOption = {
   'Billionaires':1,
   'Class Catalog - BYUI':2,
   'Country Code':3,
   'FIFA World Cup':4,
   'Financial Data':5,
   'Forbes - Billionaries':6,
   'Forbes - Universities':7,
   'Irvine Spectrum Center':8,
   'Job Board - BYUI':9,
   'Mutual App Feedback':10,
   'News - CBS':11,
   'Politicos Chilenos':12,
   'Políticos Españoles':13,
   'SINCA MMA Gob':14,
   'Surplus Store - BYUI':15,
   'US House of Representatives':16,
   'test':17
}

# st.write('You selected:', option)

## ----------------------------------------- Billionaires ------------------------------------------------------------------------ ##
if projectOption[option] == 1: #'Billionaires'
   # data = SurplusStore.data
   # url = SurplusStore.url
   # url_split = url.replace('https://','').split('/')[0]
   st.write('Billionaires')

## ----------------------------------------- Class Catalog - BYUI ------------------------------------------------------------------------ ##
elif projectOption[option] == 2:
   data = catalogBYUI.data
   url = catalogBYUI.url
   url_split = url.replace('https://','').split('/')[0]

## ----------------------------------------- Billionaires ------------------------------------------------------------------------ ##
elif projectOption[option] == 3:
   data = countryCode.data
   url = countryCode.url
   url_split = url.replace('https://','').split('/')[0]

## ----------------------------------------- Billionaires ------------------------------------------------------------------------ ##
# elif projectOption[option] == 4:
#    data = FIFAWorldCup.data
#    url = FIFAWorldCup.url
#    url_split = url.replace('https://','').split('/')[0]

## ----------------------------------------- Billionaires ------------------------------------------------------------------------ ##
elif projectOption[option] == 15:
   data = SurplusStore.data
   url = SurplusStore.url
   url_split = url.replace('https://','').split('/')[0]

## ----------------------------------------- Billionaires ------------------------------------------------------------------------ ##
elif projectOption[option] == 16: 
   data = representatives.data
   url = representatives.url
   url_split = url.replace('https://','').split('/')[0]

## ----------------------------------------- Billionaires ------------------------------------------------------------------------ ##
else:
   data = pd.DataFrame({'a':range(10)})
   url = "EXAMPLE.ORG"
   url_split = url.replace('https://','').split('/')[0]

## ----------------------------------------- Tables ----------------------------------------------------------------------------------- ##

tab1, tab2, tab3, tab4 = st.tabs(['Page', 'Table', 'Code', 'Analysis'])

with tab1:
   st.header(option)
   st.image('CatalogBYUI.png', caption='Website page')
   # f"[{url_split}]({url}) website"

with tab2:
   
   st.header(f"Data extracted from @@@")

   # st.header(f"Data extracted from {url_split}")

   st.dataframe(data)

with tab3:
   st.header("Code")

with tab4:
   st.header("Analysis")


## ----------------------------------------- Import -------------------------------------------------------------------------------------- ##
import streamlit as st

from Projects import SurplusStore
from Projects import catalogBYUI
from Projects import representatives
# from Projects import SurplusStore
# from Projects import SurplusStore
# from Projects import SurplusStore
# from Projects import SurplusStore
# from Projects import SurplusStore
# from Projects import SurplusStore


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

st.write('You selected:', option)

if projectOption[option] == 1: #'US House of Representatives'
   st.write(f"DISPLAY {projectOption[option]}")
   data = representatives.data
   url = representatives.url
   url_split = url.replace('https://','').split('/')[0]

elif option == projectOption[option]:
   data = representatives.data
   url = representatives.url
   url_split = url.replace('https://','').split('/')[0]


## ----------------------------------------- Tables ----------------------------------------------------------------------------------- ##

tab1, tab2, tab3, tab4 = st.tabs(['Page', 'Table', 'Code', 'Analysis'])

with tab1:
   st.header(option)
   f"[{url_split}]({url}) website"

with tab2:
   
   st.header(f"Data extracted from @@@")

   # st.header(f"Data extracted from {url_split}")

   # st.dataframe(data)

with tab3:
   st.header("Code")

with tab4:
   st.header("Analysis")

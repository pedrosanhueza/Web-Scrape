
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
    Author: Pedro Sanhueza \n
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

st.write('You selected:', option)

if option == 'US House of Representatives':
   
   data = representatives.data

   url = representatives.url
   
   url_split = url.replace('https://','').split('/')[0]


if option == 'Billionaires':

   import Billionaires

   Billionaires.name

   Billionaires.tableFrame()

   st.write('Billionaires imported')

## ----------------------------------------- Tables ----------------------------------------------------------------------------------- ##

tab1, tab2, tab3, tab4 = st.tabs(['Page', 'Table', 'Code', 'Analysis'])

with tab1:
   st.header(option)
   "[Open](https://alternativeto.net/) website"

with tab2:
   
   st.header(f"Data extracted from {url_split}")

   st.dataframe(data)

with tab3:
   st.header("Code")

with tab4:
   st.header("Analysis")

import streamlit as st

st.write('# Web Analysis')
st.write('''
    Author: Pedro Sanhueza
    Description: Web Scraping EDA
    ''')

options = (
    'SurplusSaleItems',
    'Forbes-Universities',
    'BYUI-JobBoard',
    'BYU-Idaho Class Catalog',
    'Forbes',
    'News',
    'Políticos Españoles',
    'Irvine Spectrum Center',
    'Politicos Chilenos',
    'FIFA World Cup',
    'SINCA MMA Gob',
    'Mutual Feedback',
    'US House of Representatives',
    'Financial Data',
    'Country Code',
    'Billionaires')



option = st.sidebar.selectbox('Web Scraping Projects', options)

st.write('You selected:', option)

if option == 'Billionaires':

   import Billionaires

   # Billionaires.tableFrame()

   st.write('Billionaires imported')

tab1, tab2, tab3, tab4 = st.tabs(['Page', 'Table', 'Code', 'Analysis'])

with tab1:
   st.header(option)
   "[Open](https://alternativeto.net/) website"

with tab2:
   st.header("Table")

with tab3:
   st.header("Code")

with tab4:
   st.header("Analysis")

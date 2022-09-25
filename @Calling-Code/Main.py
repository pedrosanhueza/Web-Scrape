import streamlit as st

# import 

st.write('# Web Analysis')
st.write('''
    Author: Pedro Sanhueza \n
    Description: Web Scraping EDA
    ''')

## ----------------------------------------- Beggin Side Bar ----------------------------------------- ##

options = (
    'Surplus Store - BYUI',
    'Forbes - Universities',
    'Job Board - BYUI',
    'Class Catalog - BYUI',
    'Forbes - Billionaries',
    'News - CBS',
    'Políticos Españoles',
    'Irvine Spectrum Center',
    'Politicos Chilenos',
    'FIFA World Cup',
    'SINCA MMA Gob',
    'Mutual App Feedback',
    'US House of Representatives',
    'Financial Data',
    'Country Code',
    'Billionaires',
    'test')

option = st.sidebar.selectbox('Web Scraping Projects', options)

## ----------------------------------------- End Side Bar ----------------------------------------- ##

st.write('You selected:', option)

if option == 'test':

   import Projects.project1 as project1

   st.write(project1.cat)

if option == 'Billionaires':

   import Billionaires

   Billionaires.name

   Billionaires.tableFrame()

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

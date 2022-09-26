
## ----------------------------------------- Import -------------------------------------------------- ##
import streamlit as st

from Projects import SurplusStore
from Projects import catalogBYUI
# from Projects import SurplusStore
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

project_id = {
   'Billionaires'          :1,
   'Class Catalog - BYUI'  :2,
   'Country Code'          :3,
   'FIFA World Cup'        :4,
   'Financial Data'        :5,
   'Forbes - Billionaries' :6,
   'Forbes - Universities' :7,
   'Irvine Spectrum Center':8,
   'Job Board - BYUI'      :9,
   'Mutual App Feedback'   :10,
   'News - CBS'            :11,
   'Politicos Chilenos'    :12,
   'Políticos Españoles'   :13,
   'SINCA MMA Gob'         :14,
   'Surplus Store - BYUI'  :15,
   'US House of Representatives':16,
   'test'                  :17}

## ----------------------------------------- Beggin Side Bar ----------------------------------------- ##

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

## ----------------------------------------- Modules Variables ------------------------------------ ##

with st.container():
   st.components.v1.html('https://docs.streamlit.io/en/latest')


if project_id[option] == 1:
   from Projects import SurplusStore

elif project_id[option] == 2:
   from Projects import catalogBYUI

elif project_id[option] == 3:
   st.write('b')

elif project_id[option] == 4:
   st.write('b')

elif project_id[option] == 5:
   st.write('b')

elif project_id[option] == 6:
   st.write('b')

elif project_id[option] == 7:
   st.write('b')

elif project_id[option] == 8:
   st.write('b')

elif project_id[option] == 9:
   
   from Projects import jobBoardBYUI

   data = jobBoardBYUI.data

   st.dataframe(data)

elif project_id[option] == 10:
   st.write('b')

elif project_id[option] == 11:
   st.write('b')

elif project_id[option] == 12:
   st.write('b')

elif project_id[option] == 13:
   st.write('b')

elif project_id[option] == 14:
   st.write('b')

elif project_id[option] == 15:
   st.write('SurplusStore')
   
   from Projects import SurplusStore



elif project_id[option] == 16:
   st.write('b')

elif project_id[option] == 17:
   st.write('b')

else:
   data = pd.DataFrame({'a':1})

## ----------------------------------------- Modules Variables ------------------------------------ ##

st.write('You selected:', option)

if option == 'test':

   st.dataframe(data)

if option == 'Billionaires':

   import Billionaires

   Billionaires.name

   Billionaires.tableFrame()

   st.write('Billionaires imported')

## ----------------------------------------- Tables ----------------------------------------------- ##

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

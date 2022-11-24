## ----------------------------------------- Import -------------------------------------------------------------------------------------- ##
import streamlit as st
import streamlit.components.v1 as components # embed website
import pandas as pd # panel data

from datetime import datetime, timedelta
import time

import pytz
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import plotly.express as px
from plotly.figure_factory import create_distplot

import os

st.set_option('deprecation.showPyplotGlobalUse', False)

## ----------------------------------------- Introduction ----------------------------------------------------------------------------- ##

st.markdown('''
<h1 style="font-size:40px;text-align:center;"> Hi there! </h1>
''',unsafe_allow_html=True)

col1, col2, col3 = st.columns([2,3,1])
with col1:
   st.write(' ')
with col2:
   st.image('@Calling-Code/Pictures/Me_sticker.png', caption='Profile Sticker', width=300) 
with col3:
   st.write(' ')

st.markdown('''
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">

<p style="font-size:20px;text-align:center;">
   Select a project from the drop-down bar.
   <br>
   Feel free to connect with me on 
   <a href="https://www.linkedin.com/in/pedro-sanhueza/"> Linked-In</a>
</p>

''',unsafe_allow_html=True)

# col1, col2, col3 = st.columns([1.5,3,1.5])
# with col1:
#     st.write(' ')
# with col2:
#    st.image('@Calling-Code/Pictures/API_call_3.gif') 
# with col3:
#     st.write(' ')
   
st.markdown('''<hr>''',unsafe_allow_html=True)

## ----------------------------------------- Begining Side Bar ----------------------------------------------------------------------------- ##

st.markdown('''
<h1 style="font-size:40px;text-align:center;"> Web Scraping Projects </h1> 
''',unsafe_allow_html=True)

projectOption = {
   'Select a project':1,
   'BYU-Idaho Class Catalog':2,
   'Phone Country Code':3,
   'FIFA Soccer 2022':4,
   'Stocks - ADVFN':5,
   'Billionaires - Forbes':6,
   'Universities - Forbes':7,
   'Irvine Spectrum Center - Stores':8,
   'BYU-Idaho Student Employment':9,
   'Mutual App Feedback':10,
   'News - CBS':11,
   'Politicos Chilenos':12,
   'Políticos Españoles':13,
   'SINCA MMA Gob':14,
   'Surplus Store - BYUI':15,
   'Representatives - USA':16,
   'Boat Trader':17}

projects = tuple(projectOption.keys())

project = st.selectbox('Select project: ', projects)

## ----------------------------------------- General Variables ------------------------------------------------------------------------ ##

project_order = list(projectOption.values())

IdahoTz = pytz.timezone('US/Mountain') 
timeZoneMountain = datetime.now(IdahoTz)
currentTimeInRexburg = timeZoneMountain.strftime("%Y-%m-%d")
YesterdayTimeInRexburg = (timeZoneMountain - timedelta(1)).strftime("%Y-%m-%d")

## ----------------------------------------- TEST ------------------------------------------------------------------------ ##
if projectOption[project] == 1:
   st.write(project)

   url1 = 'https://www.boattrader.com/boat-dealers/'
   url5 = 'https://www.irvinespectrumcenter.com/shopping/stores'
   url7 = 'https://www.cbsnews.com/world/'
   url11= 'https://web.byui.edu/SurplusList/'
   url12= 'https://www.byui.edu/catalog#/courses'
   
   st.markdown(f'''
   <h1 style="font-size:30px;text-align:center;"> What is Web Scraping? </h1>
   <p>
      Web scraping is an automatic method to obtain large amounts of data from websites.
      It is a form of copying specific data gathered from the web, most of this data is unstructured data in an HTML format which is then converted into structured data in a spreadsheet or a database for later retrieval or analysis.
   </p>
   <h1 style="font-size:30px;text-align:center;"> How  Web Scrapers Work? </h1>
   <p>
      A web scraper first needs the URLs to scrape a site. Then it loads all the HTML code for those sites
      Then the scraper obtains the required data from this HTML code and outputs this data in the format specified by the client.
      Mostly, this is in the form of an Excel spreadsheet or a CSV file.
   </p>
   ''',unsafe_allow_html=True)

   col1, col2, col3 = st.columns([1,3,1])
   with col1:
      st.write(' ')
   with col2:
      st.image('@Calling-Code/Pictures/API_call_3.gif', caption='Scraping Process') 
   with col3:
      st.write(' ')

## ----------------------------------------- Class Catalog - BYUI ------------------------------------------------------------------------ ##
if projectOption[project] == 2:
   from Projects._2_BYUI_ClassCatalog import catalogBYUI
   url = catalogBYUI.url_display
   data = catalogBYUI.data
   script_1 = catalogBYUI.script_1

   st.markdown(f'''
   <br><p style="font-size:20px;text-align:left;">
      Extracting data from: 
      <a style="color:#4F9ACF; padding:7px 10px;" target="_blank" href = '{url}'> Class Catalog - BYUI </a>
   </p>
   ''',unsafe_allow_html=True)
   
   st.markdown(f'''
         <h1 style="font-size:40px;text-align:center;"> Description: </h1>
         <p style="font-size:20px;text-align:Center;">
            The
            <a href='{url}' style="color:#4F9ACF;" >University's catalog </a>
            website has the list of all classes offered and its Course ID, Title, Activation Date, Department, and more.
            There are about {data.shape[0]} courses and {data.shape[1]} descriptions for each course.
            <br>
            This code extract all that data and puts it into a local CSV file.
         </p>
      <br>
   ''',unsafe_allow_html=True)

   with st.expander("Code Used 🐍"):
      st.code(script_1,language="python")
   with st.expander("See Website 👨🏻‍💻"):
      components.iframe(f"{url}",width=1000, height=500, scrolling=True)
   with st.expander("Data Extracted 🕸"):
      st.write("Table containing data extracted from website")
      
      st.download_button(
         label     =    "Download data as CSV",
         data      =    data.to_csv().encode('utf-8'),
         file_name =    'Class_Catalog_BYUI.csv',
         mime      =    'text/csv',)
      
      st.dataframe(data)

   st.markdown(f'''<br><br><br><br><br>''',unsafe_allow_html=True)

# ## ----------------------------------------- # Country Code ------------------------------------------------------------------------ ##
if projectOption[project] == 3:
   with st.spinner('Web scraping data from website ...'):
      from Projects._3_CountryCode import countryCode
   url = countryCode.url
   script_1 = countryCode.script_1
   data = countryCode.data
   data_1 = countryCode.df1
   data_2 = countryCode.df2

   st.markdown('''
   <center>
      <img src='https://countrycode.org/static/images/map_970da81.png' alt="Logo" width="100%">
   </center>
   ''',unsafe_allow_html=True)

   st.markdown(f'''
   <h1 style="font-size:40px;text-align:center;"> Description: </h1>
   <p style="font-size:20px;text-align:center;">
      <a href='{url}' style="color:#4F9ACF;" > Country Code </a>
      is a complete guide to call anywhere in the world.
      The calling chart has dialing codes to make long distance phone calls around the globe.
      <br><br>
      The following python code extracts the table from the website and stores it into a local CSV file.
   </p>
   ''',unsafe_allow_html=True)

   with st.expander("Code Used 🐍"):
      st.code(script_1,language="python")
   with st.expander("Data Extracted 🕸"):
      st.write("Table containing data extracted from website")
      st.download_button(
         label     =    "Download data as CSV",
         data      =    data.to_csv().encode('utf-8'),
         file_name =    'Country_Phone_Code.csv',
         mime      =    'text/csv',)
      st.dataframe(data)
   with st.expander("Analysis 🧐"):
      st.bar_chart(data=data_1, x='Country', y='GDP_USD')
      st.bar_chart(data=data_2, x='Country', y='Population')
      st.vega_lite_chart(data, {
      'mark': {'type': 'circle', 'tooltip': True},
      'encoding': {
         'x': {'field': 'Area_KM2', 'type': 'quantitative'},
         'y': {'field': 'Population', 'type': 'quantitative'},
         # 'size': {'field': 'c', 'type': 'quantitative'},
         'color': {'field': 'Area_KM2', 'type': 'quantitative'},
      },})
      KPI1, KPI2, KPI3 = st.columns(3)
      KPI1.metric('Countries', data.Country.nunique())
      KPI2.metric('Highest GDP', data_1.sort_values('GDP_USD').tail(1)['Country'].iloc[0])
      KPI3.metric('Highest Population', data.sort_values('Population').tail(1)['Country'].iloc[0])

# ## ----------------------------------------- FIFA World Cup ------------------------------------------------------------------------ ##
if projectOption[project] == 4:
   with st.spinner('Web scraping data from website ...'):
      from Projects._4_FIFAWorldCup import FIFAWorldCup
   url = FIFAWorldCup.url
   data = FIFAWorldCup.data
   script_1 = FIFAWorldCup.script_1

   logo_url = 'https://upload.wikimedia.org/wikipedia/en/thumb/e/e3/2022_FIFA_World_Cup.svg/1200px-2022_FIFA_World_Cup.svg.png'

   st.markdown(f'''
   <center>
      <img src={logo_url} alt="Logo" width="100%">
   </center>
   ''',unsafe_allow_html=True)

   st.markdown(f'''
   <h1 style="font-size:40px;text-align:center;"> Description: </h1>
   <p style="font-size:20px;text-align:center;">
      <a href='{url}' style="color:#4F9ACF;" > Fox Sports </a>
      has a complete list of all teams and players in the FIFA World Cup 2022.
      This python code organizes the data from various pages within this website and merges them all together into one big dataset.
      <br><br>
      
   </p>
   ''',unsafe_allow_html=True)

   with st.expander("Code Used 🐍"):
      st.code(script_1,language="python")

   with st.expander("Data Extracted 🕸"):
      st.write("Table containing data extracted from website")
      st.download_button(
         label     =    "Download data as CSV",
         data      =    data.to_csv().encode('utf-8'),
         file_name =    'Soccer_Teams_2022.csv',
         mime      =    'text/csv',)
      st.dataframe(data)
      st.info('Refresh the page if table is not showing up', icon="ℹ️")
      st.warning("www.FoxSports.com is a highly protected websited, contact me if you're not able to see the complete table", icon="⚠️")

#    data_main = data.copy()
   
#    countries = ('All Countries',) + tuple(data.Country.unique())
#    country_selected = st.sidebar.selectbox("Countries",countries)

#    positions = ('All Positions',) + tuple(data.POS.unique())
#    position_selected = st.sidebar.selectbox("Positions",positions)

#    if country_selected != 'All Countries':
#       data_main = data[data.Country == country_selected]
#       url_pic_country = data_main.Country_logo.iloc[0]

#    if position_selected != 'All Positions':
#       data_main = data[data.POS == position_selected]
#       url_pic_country = data_main.Country_logo.iloc[0]

#    if (country_selected != 'All Countries') and (position_selected != 'All Positions'):
#       data_main = data[(data.POS == position_selected) & (data.Country == country_selected)]
   
#    if (country_selected == 'All Countries') and (position_selected != 'All Positions'):
#       data_main = data[data.POS == position_selected]
   
   
#    st.image(f"{url_pic}",width=400)

#    Players_avg = round(1 - data_main.shape[0] / (data.shape[0] / data.Country.nunique())  - 1,2)
#    Age_avg =     round(1 - data.AGE.mean() / data[data.Country == country_selected].AGE.mean(),2)
#    HT_avg =      round(1 - data.HT.mean()  / data[data.Country == country_selected].HT.mean() ,2)
#    WT_avg =      round(1 - data.WT.mean()  / data[data.Country == country_selected].WT.mean() ,2)
#    BMI_avg =     round(1 - data.BMI.mean()  / data[data.Country == country_selected].BMI.mean(),2)

#    tab1, tab2, tab3, tab4 = st.tabs(['Overview', 'Table', 'Code', 'Analysis'])

#    with tab1:
#       col2, col3, col4, col5, col6 = st.columns(5)
#       if country_selected == 'All Countries':
#          col2.metric("Players",    round(data_main.shape[0]))
#          col3.metric("Age Avg",    round(data_main.AGE.mean()))
#          col4.metric("Height Avg", round(data_main.HT.mean()))
#          col5.metric("Weight Avg", round(data_main.WT.mean()))
#          col6.metric("BMI Avg",    round(data_main.BMI.mean()))
#       else:
#          col2.metric("Players",    round(data_main.shape[0]), str(Players_avg) + '%')
#          col3.metric("Age Avg",    round(data_main.AGE.mean()), str(Age_avg) + "%")
#          col4.metric("Height Avg", round(data_main.HT.mean()), str(HT_avg)  + "%")
#          col5.metric("Weight Avg", round(data_main.WT.mean()), str(WT_avg)  + "%")
#          col6.metric("BMI Avg",    round(data_main.BMI.mean()), str(BMI_avg) + "%")

#          st.image(f"{url_pic_country}",width=400)

#    with tab2:
#       if (country_selected != 'All Countries' or position_selected != 'All Positions'):
#          st.dataframe(data_main.drop('Country_logo', axis=1))
#       else:
#          st.dataframe(data.drop('Country_logo', axis=1))
#    with tab3:
#       st.header('Code for live data extraction')
#       st.write('Runs every time you load the page and updates the table')
#       st.code(FIFAWorldCup.script, language="python")
#    with tab4:
#       st.header(option)

## ----------------------------------------- Financial Data ------------------------------------------------------------------------ ##
if projectOption[project] == 5:
   # from Projects._5_Financial Data import 
   # st.write(.url)
   # data = .data
   # st.dataframe(data)
   col1, col2, col3 = st.columns([2,3,1])
   with col1:
      st.write(' ')
   with col2:
      st.image('@Calling-Code/Pictures/under-construction.gif', caption='Coming Soon', width=300) 
   with col3:
      st.write(' ')


## ----------------------------------------- Forbes Billionaires ------------------------------------------------------------------------ ##
if projectOption[project] == 6:
   with st.spinner('Web scraping data from website ...'):
      from Projects._6_ForbesBillionaries import forbesBillionaires
   url_main = forbesBillionaires.url_main 
   script_1 = forbesBillionaires.script_1
   data = forbesBillionaires.data
   
   st.write(url_main)

   st.markdown('''
   <center>
      <img src='https://thumbor.forbes.com/thumbor/1500x0/smart/filters:format(jpeg)/https%3A%2F%2Fimages.forbes.com%2FBillies22%2Flanding-1500px.gif' alt="Logo" width=50%>
   </center>
   ''',unsafe_allow_html=True)

   st.markdown(f'''
   <h1 style="font-size:40px;text-align:center;"> Description: </h1>
   <p style="font-size:20px;text-align:center;">
      Forbes is an American business magazine. It features articles on finance, industry, investing, and marketing topics.
      It is best known for its lists, which rank billionaires, colleges, real estate, and entertainers, to name a few.
   <br><br>
      In this project, I extract the data from <a href="{url_main}"> The Richest People In The World </a> along with their key attributes such as 
      Name, Net Worth, Age, Country, Source of Wealth, and Education Level (bachelor's, master's, PhD, etc).
      <br><br>
      Here is the web scraping code, and table with data extracted:
   </p>
   ''',unsafe_allow_html=True)

   with st.expander("Code Used 🐍"):
      st.code(script_1,language="python")
   with st.expander("Data Extracted 🕸"):
      st.write("Table containing data extracted from website")
      st.download_button(
         label     =    "Download data as CSV",
         data      =    data.to_csv().encode('utf-8'),
         file_name =    'Forbes_Billionaires_list.csv',
         mime      =    'text/csv',)
      st.dataframe(data)
   st.markdown(f'''<br><br><br><br><br>''',unsafe_allow_html=True)

## ----------------------------------------- Forbes Universities ------------------------------------------------------------------------ ##
if projectOption[project] == 7:
   with st.spinner('Web scraping data from website ...'):
      from Projects._7_ForbesUniversities import Forbes_Universities
   url_main = Forbes_Universities.url_main
   data = Forbes_Universities.data
   script_1 = Forbes_Universities.script_1

   st.markdown('''
   <center>
      <img src='https://www.forbes.com/dam/imageserve/630e5f2f3d58f237d14c94f4/x.jpg' alt="Logo" width=50%>
   </center>
   ''',unsafe_allow_html=True)

   st.markdown(f'''
   <h1 style="font-size:40px;text-align:center;"> Description: </h1>
   <p style="font-size:20px;text-align:center;">
      Forbes is an American business magazine. It features articles on finance, industry, investing, and marketing topics.
      It is best known for its lists, which rank billionaires, colleges, real estate, and entertainers, to name a few.
   <br><br>
      In this project, I extract the data from <a href="{url_main}"> America's Top Colleges List </a> along with their key attributes such as 
      Student Population, Median Base Salary, Contact Information, Web Site, Social Media, and University Type (private or public).
      <br><br>
      Here is the web scraping code, table with data extracted, and analysis:
   </p>
   ''',unsafe_allow_html=True)

   with st.expander("Code -- Python 🐍"):
      st.code(script_1, language="python")

   with st.expander("Data Extracted 🕸"):
      # st.write("Table containing data extracted from website")
      st.download_button(
         label     =    "Download data as CSV",
         data      =    data.to_csv().encode('utf-8'),
         file_name =    'America_Top_Colleges.csv',
         mime      =    'text/csv',)
      st.dataframe(data)

## ----------------------------------------- Irvine Spectrum Center ------------------------------------------------------------------------ ##
if projectOption[project] == 8:
   with st.spinner('Web scraping data from website ...'):
      from Projects._8_IrvineSpectrumCenter import irvinespectrumcenter
   url_main = irvinespectrumcenter.url_main
   url_main_1 = irvinespectrumcenter.url_main_1
   data = irvinespectrumcenter.data
   script_1 = irvinespectrumcenter.script_1

   st.markdown('''
   <center>
      <img src='https://www.irvinespectrumcenter.com/media/2158/isc-general-holiday-tablet-1550x924.jpg?' alt="Logo" width=50%>
   </center>
   ''',unsafe_allow_html=True)

   st.markdown(f'''
   <h1 style="font-size:40px;text-align:center;"> Description: </h1>
   <p style="font-size:20px;text-align:center;">
      The Irvine Spectrum Center is an outdoor shopping center developed by the Irvine Company, located in the Irvine Spectrum district on the southeast edge of Irvine, California.
      The mall features Nordstrom and Target department stores, a ferris wheel, and a Regal Cinemas 21-screen movie theater.
   <br><br>
      In this project, I extract the store's information from <a href="{url_main}"> Irvine Spectrum Center </a>,
      particularly the <a href="{url_main_1}"> stores list </a>
      extracting key attributes such as the store name, Phone, location in the mall, category type (dining or shopping), and if the store has deals or not.
      <br><br>
      Here is the web scraping code, and table with data extracted:
   </p>
   ''',unsafe_allow_html=True)

   with st.expander("Code -- Python 🐍"):
      st.code(script_1, language="python")
   
   with st.expander("Data Extracted 🕸"):
      # st.write("Table containing data extracted from website")
      st.download_button(
         label     =    "Download data as CSV",
         data      =    data.to_csv().encode('utf-8'),
         file_name =    'irvinespectrumcenter_stores.csv',
         mime      =    'text/csv',)
      st.dataframe(data)
# ## ----------------------------------------- Job Board - BYUI ------------------------------------------------------------------------ ##
if projectOption[project] == 9:

   col1, col2, col3 = st.columns([2,3,1])
   with col1:
      st.write(' ')
   with col2:
      st.image('@Calling-Code/Pictures/under-construction.gif', caption='Coming Soon', width=300) 
   with col3:
      st.write(' ')
   # from Projects._9_BYUI_JobBoard import BYUI_JobBoard
#    st.write(project)
   
#    st.markdown('''
#    <p style="text-align:right;">
#       Author: Pedro Sanhueza
#    </p>
   
#    <center>
#       <h1 style="color:#214491;font-size: 90px;">
#          BYU-I
#          <br>
#          Job Board 
#       </h1>
#    </center>
   
#    <br>
#   ''',unsafe_allow_html=True)

#    data = BYUI_JobBoard.data
   
#    d = str(datetime.today().strftime("%Y-%m-%d"))

#    KPI1_jobs = round(1-(400/data.shape[0]),2)

#    KPI1_1_max = round(1-(data.payRate.median()/data.payRate.max()),2)

#    today_data = data[data.dateUpdated >= currentTimeInRexburg]

#    today = today_data.shape[0]

#    yesterday_data = data[data.dateUpdated == (datetime.today() - timedelta(1)).strftime("%Y-%m-%d")]

#    yesterday = yesterday_data.shape[0]

#    KPI1, KPI2, KPI3, KPI4 = st.columns(4)

#    KPI1.metric('Jobs Published', f"{data.shape[0]}")

#    KPI2.metric("Departments Recluting", f"{data.departmentName.nunique()}")

#    KPI3.metric("Jobs Posted Today",today)

#    KPI4.metric("Highest Pay Rate Job", f"${data.payRate.max()}")

#    st.markdown('''
#    <br>
#    <p style="font-size:40px;text-align:center;color:#4F9ACF;">
#       Highest Paid Jobs
#    </p>
#    <br>
#    ''',unsafe_allow_html=True)

#    Njobs = st.slider('Select a range of jobs', 1, 10, 5)

#    data_topPayRate = data.sort_values('payRate', ascending=False).head(Njobs)[['title','payRate','departmentName','managerName','URL']]
   
#    data_topPayRate.columns = ['Job Title','Hourly Wage','Department','Employer','Application Link']

#    st.dataframe(data_topPayRate.reset_index().drop('index',axis=1))

#    if today > 0:

#       st.markdown(f'''
#       <br>
#       <p style="font-size:40px;text-align:center;color:#4F9ACF;">
#          Jobs Posted Today
#       </p>
#       <p style="text-align:center;color:#4F9ACF;">
#          {currentTimeInRexburg}
#       </p>
#       <br>
#       ''',unsafe_allow_html=True)

#       st.dataframe(today_data[['title','payRate','departmentName','managerName','URL']].sort_values('payRate',ascending=False))
#    elif yesterday > 0:
#       st.markdown(f'''
#       <br>
#       <p style="font-size:40px;text-align:center;color:#4F9ACF;">
#          Jobs Posted Yesterday
#       </p>
#       <p style="text-align:center;color:#4F9ACF;">
#          {YesterdayTimeInRexburg}
#       </p>
#       <br>
#       ''',unsafe_allow_html=True)

#       st.dataframe(yesterday_data[['title','payRate','departmentName','managerName','URL']].sort_values('payRate',ascending=False))

#    st.markdown('''
#    <br>
#    <p style="font-size:40px;text-align:center;color:#4F9ACF;">
#       Pay Rate Distribution
#    </p>
#    <br>
#    ''',unsafe_allow_html=True)

#    col1, col2 = st.columns([4,1])

#    with col2:
#       job_type = st.radio("Job Type", ('All','Online','On-Campus'))
      
#       if job_type == 'Online':
#          data_isOnline = data[data.isOnline == True]
#       elif job_type == 'On-Campus':
#          data_isOnline = data[data.isOnline == False]
#       else:
#          data_isOnline = data.copy()

#    with col1:   
#       sns.kdeplot(data_isOnline.payRate, shade=True, color="#214491", bw=0.8, alpha=0.5, cut=0)
#       fig1 = plt.show()
#       st.pyplot(fig1)

#    tab1, tab2 = st.tabs(['Data','Code'])

#    with tab1:
#       columns_ls = st.multiselect(
#       '',
#       data.columns,
#       ['title', 'payRate','managerName'])

#       st.dataframe(data[columns_ls])

#       @st.cache
#       def convert_df(df):
#          # IMPORTANT: Cache the conversion to prevent computation on every rerun
#          return df.to_csv().encode('utf-8')

#       csv = convert_df(data)

#       file_name = 'BYUI_jobBoard_' + str(time.strftime("%Y-%m-%d"))

#       st.download_button(
#          label = "Download data as CSV",
#          data = csv,
#          file_name = file_name,
#          mime = 'text/csv')

#    with tab2:

#       st.markdown(f'''
#       <br>
#       <p style="font-size:20px;text-align:center;color:#4F9ACF;">
#          🐍 Source Code
#       </p>
#       <a style="color:#4F9ACF; padding:7px 10px;"
#          target="_blank" 
#          href = 'https://github.com/pedrosanhueza/Web_Scrape/blob/main/BYUI_JobBoard/Job_board-Code/API-call-JobBoard.ipynb'>
#          GitHub Repository
#       </a>
#       <br>
#       ''',unsafe_allow_html=True)

#       st.code(BYUI_JobBoard.script1, language='python')
   
   # with tab1:
   #    col1, col2, col3 = st.columns(3)

   #    with col1:
   #       st.write('')
   #    with col2:
   #       st.write(data.payRate.max(), 12,13)
   #    with col3:
   #       st.write('')

   # with tab2:
   #    jobs_to_remove = ['TA','Custodian','Online','Grounds']
   #    jobs_to_remove_str = '|'.join(jobs_to_remove)   
   #    st.write('Personalised Table')
   #    data_p = data[~data.title.str.contains(jobs_to_remove_str)].sort_values('payRate', ascending=False)[['title','payRate','workSchedule','URL']]
   #    st.dataframe(data_p)
      
   #    sns.kdeplot(data.payRate, shade=True, color="g", bw=0.94, alpha=0.5, cut=0)
   #    fig1 = plt.show()
   #    st.pyplot(fig1)

   # with tab3:
   #    st.dataframe(BYUI_JobBoard.data)

   # with tab4:
   #    st.code(BYUI_JobBoard.script1)

   # sns.kdeplot(data.payRate, shade=True, color="g", bw=0.8, alpha=0.5, cut=0)

   # fig1 = plt.show()

   # st.pyplot(fig1)

   # if st.button('Personalised Table'):
   #    jobs_to_remove = ['TA','Custodian','Online','Grounds']
   #    jobs_to_remove_str = '|'.join(jobs_to_remove)   
   #    st.write('Personalised Table')
   #    data_p = data[~data.title.str.contains(jobs_to_remove_str)].sort_values('payRate', ascending=False)[['title','payRate','workSchedule','URL']]
   #    st.table(data_p)

   # if st.button("ballons"):
   #    st.balloons()
   
   # if st.button("info"):
   #    st.info('This is a purely informational message', icon="ℹ️")

## ----------------------------------------- Mutual App Feedback ------------------------------------------------------------------------ ##

if projectOption[project] == 10:

   st.info('''
   feedback.mutual.app allows a few data requests per hour ...
   If you run into a TCP port 443 error, is the default port used by HTTPS.
   This means that the port is blocked on any server or device from your browser to the website: https://feedback.mutual.app/''', icon="ℹ️")

   from Projects._10_MutualAppFeedback import Mutual_App_Feedback

   data = Mutual_App_Feedback.data
   data_1 = Mutual_App_Feedback.data_1
   table_1 = Mutual_App_Feedback.table_1
   data_2 = Mutual_App_Feedback.data_2
   logo = Mutual_App_Feedback.logo
   scrpt_1 = Mutual_App_Feedback.script_1
   url_base = Mutual_App_Feedback.url_base

   st.markdown(f''' <center> <br> <img src="{logo}"> <br><br><br> </center> ''',unsafe_allow_html=True)

   tab1, tab2, tab3 = st.tabs(["Analysis 🧐", "Script 🐍","Table 🥩"])
   with tab1:
      col1, col2, col3, col4 = st.columns(4)
      col1.metric("Total Suggestions", f"{data.id.count()}")
      col2.metric("Suggestions Rejected",f"{data.status.str.contains('Close').sum()}")
      col3.metric("Suggestions Addded",f"{data.status.str.contains('Released').sum()}")
      col4.metric("Highest Interact Month", f"{data.date_created_month.value_counts().index[0]}")

      st.markdown(f'''<h1 style="font-size:30px;text-align:center;"> Votes per Month: </h1>''',unsafe_allow_html=True)
      st.bar_chart(data=data_1, x='index', y='date_created_month')
      st.markdown(f'''<h1 style="font-size:30px;text-align:center;"> Top 10 votes features not done: </h1>''',unsafe_allow_html=True)
      st.table(table_1)
      st.markdown(f'''<h1 style="font-size:30px;text-align:center;"> Feedbacks per Status </h1>''',unsafe_allow_html=True)
      st.bar_chart(data=data_2, x='index', y='status')

   with tab2:
      st.markdown(f'''<a href="{url_base}"> feedback.mutual.app </a>''',unsafe_allow_html=True)
      st.code(scrpt_1, language='python')
   with tab3:
      st.markdown(f'''<a href="{url_base}"> feedback.mutual.app </a>''',unsafe_allow_html=True)
      st.download_button(
      label     =    "Download data as CSV",
      data      =    data.to_csv().encode('utf-8'),
      file_name =    'Mutual_App_Feedback.csv',
      mime      =    'text/csv',)
      st.dataframe(data)

## ----------------------------------------- News CBS ------------------------------------------------------------------------ ##
if projectOption[project] == 11:
   from Projects._11_NewsCBS import cbsnews
   url_main = st.write(cbsnews.url_main)
   data = cbsnews.data
   script_1 = cbsnews.script_1
   
   with st.expander("Code Used 🐍"):
      st.code(script_1,language="python")
   with st.expander("Data Extracted 🕸"):
      st.write("Table containing data extracted from website")
      st.download_button(
         label     =    "Download data as CSV",
         data      =    data.to_csv().encode('utf-8'),
         file_name =    'cbsnews.csv',
         mime      =    'text/csv',)
      st.dataframe(data)

## ----------------------------------------- Politicos Chilenos - Camara Diputados ------------------------------------------------------------------------ ##
if projectOption[project] == 12:
   from Projects._12_PoliticosChilenos.camara_diputados import url_main
   from Projects._12_PoliticosChilenos.camara_diputados import data_simple
   from Projects._12_PoliticosChilenos.camara_diputados import ID_options
   from Projects._12_PoliticosChilenos.camara_diputados import script_1

   data_1 = data_simple

   st.write(url_main)
   st.dataframe(data_1)

   ID_option = st.select_slider('Select a color of the rainbow', options = ID_options)

   url_img = data_1[data_1.ID == ID_option]['img'].iloc[0]
   url_profile = data_1[data_1.ID == ID_option]['website'].iloc[0]

   st.markdown(f'''
      <br>
      <center>
      <img src="{url_img}">
      </center>
      ''',unsafe_allow_html=True)
   
   st.write(url_profile)
   st.table(data_simple[data_simple.ID == ID_option].iloc[:,:-2])
   st.markdown(f'''<h1 style="font-size:40px;text-align:center;"> Scraping Code: </h1>''',unsafe_allow_html=True)
   st.code(script_1,language="python")


## ----------------------------------------- Politicos Españoles - Camara Diputados ------------------------------------------------------------------------ ##
if projectOption[project] == 13:
   from Projects._13_PoliticosEspanoles import DiputadosEspanoles
   st.write(DiputadosEspanoles.url_main)
   data = DiputadosEspanoles.data
   st.dataframe(data)

## ----------------------------------------- Politicos Españoles - Camara Diputados ------------------------------------------------------------------------ ##
if projectOption[project] == 14:
   from Projects._14_SINCAMMAGob import SINCAMMAGob
   data = SINCAMMAGob.data
   url_main = SINCAMMAGob.url_main

## ----------------------------------------- Surplus Store ------------------------------------------------------------------------ ##
if projectOption[project] == 15:
   from Projects._15_BYUI_SurplusStore import SurplusStore

   st.write(SurplusStore.url)
   data = SurplusStore.data
   data_1 = SurplusStore.data_1
   data_2 = SurplusStore.data_2
   # data_1_names = SurplusStore.data_1_names
   # data_1_values = SurplusStore.data_1_values

   st.markdown('''
      <p style="text-align:right;">
         Author: Pedro Sanhueza
      </p>

      <center>
         <h1 style="color:#214491;font-size: 90px;">
            BYU-I
            <br>
            Surplus Store
         </h1>
      </center>

      <br>
   ''',unsafe_allow_html=True)

   highest_price = '$' + str( round(data.Price.max(),2))
   price_mean = '$' + str( round(data.Price.mean(),2) )
   excellent_items = str(data[data.Condition == 'Excellent'].shape[0]) + ' Items'
   KPI1, KPI2, KPI3, KPI4 = st.columns(4)
   KPI1.metric('Items in Store', f"{data.shape[0]}")
   KPI2.metric('Higher Price Item', f"{highest_price}")
   KPI3.metric('Average Price', f"{price_mean}")
   KPI4.metric('Excellent Condition', f"{excellent_items}")
   st.dataframe(data)
   
   st.bar_chart(data_1, y='Condition', x='index')
   st.table(data_1)
   st.bar_chart(data_2, x='Description', y='Price')
   st.table(data_2)
   condition_option = st.select_slider('Select a color of the rainbow', options = data.Condition.unique())
   data_3 = data_2[data_2.Condition == condition_option]
   st.table(data_3)

# ## -----------------------------------------  ------------------------------------------------------------------------ ##
if projectOption[project] == 16:
   st.write(project)
   from Projects._16_USHouseRepresentatives import representatives

   # data = representatives.rows
   # st.dataframe(data)
   data = representatives.data
   st.dataframe(data)



   # st.markdown('''
   #    <p style="text-align:right;">
   #       Author: Pedro Sanhueza
   #    </p>

   #    <center>
   #       <h1 style="color:#214491;font-size: 90px;">
   #          UNITED STATES
   #          <br>
   #          HOUSE of
   #          <br>
   #          REPRESENTATIVES
   #       </h1>
   #    </center>

   #    <br>
   # ''',unsafe_allow_html=True)

   # st.markdown('''
   # <center>
   #    <p style="font-size:30px;">
   #       <b> Part 1/3: </b>
   #       Web Scraping Data Extraction 🐍
   #    </p>
   # </center>
   # ''',unsafe_allow_html=True)

   # st.code(representatives.script1, language='python')
   
   # st.markdown('''
   # <center>
   #    <p style="font-size:30px;">
   #       Code Extraction Output
   #    </p>
   # </center>
   # ''',unsafe_allow_html=True)

   # st.dataframe(data)

   # st.markdown('''
   # <center>
   #    <p style="font-size:30px;">
   #       <b> Part 2/3: </b>
   #       Explanatory Data Analysis
   #    </p>
   # </center>
   # ''',unsafe_allow_html=True)

   # data_melt_committee = data.copy()
   # data_melt_committee[[0,1,2,3,4,5]] = data['Committee Assignment'].str.split('|',expand=True)
   # data_melt_committee.drop('Committee Assignment',axis=1, inplace=True)
   # data_melt_committee = data_melt_committee.melt(id_vars=['District','Name','Party','Office Room','Phone','State'],value_name='Committee Assignment')
   # data_melt_committee = data_melt_committee[~data_melt_committee['Committee Assignment'].isnull()].drop('variable',axis=1)

   # KPI1,KPI2,KPI3,KPI4,KPI5 = st.columns(5)
   # KPI1.metric('Districts', f"{data.District.nunique()}")
   # KPI2.metric('Representatives', f"{data.Name.nunique()}")
   # KPI3.metric('Parties', f"{data.Party.nunique()}")
   # KPI4.metric('Committees', f"{data_melt_committee['Committee Assignment'].nunique()}")
   # KPI5.metric('States', f"{data.State.nunique()}")

   # newnames = {'R':'Republicans','D':'Democrats'}
   # fig = px.pie(data['Party'].replace(newnames),names='Party',color='Party',color_discrete_map={'Republicans':'Red','Democrats':'Blue'})
   # fig.update_traces(textfont_size=22,textinfo='percent+value')
   # fig.update_layout(legend=dict(
   #  orientation="h",
   #  yanchor="bottom",
   #  y=1.02,
   #  xanchor="right",
   #  x=0.67))
   # st.plotly_chart(fig,use_container_width=True)

   # st.bar_chart(data.State.value_counts().reset_index(), y='State',x='index')

   # party_group = st.radio("Representative Members by State",('Both','Republicans','Democrats'), horizontal=True)

   # if party_group == 'Republicans':
   #    fig = px.bar(data[data.Party=='R'],x='State',color='Party',color_discrete_map={'R': 'red'},width=900,height=400,labels={'count': 'Amount'})
   #    fig.update_layout(xaxis={'categoryorder':'total descending'})
   #    fig.update_xaxes(tickangle=-45)
   #    newnames = {'R':'Republicans'}
   #    fig.for_each_trace(lambda t: t.update(name = newnames[t.name]))
   #    st.plotly_chart(fig)

   # elif party_group == 'Democrats':
   #    fig = px.bar(data[data.Party=='D'],x='State',color='Party',color_discrete_map={'D': 'Blue'},width=900,height=400,labels={'count': 'Amount'})
   #    fig.update_layout(xaxis={'categoryorder':'total descending'})
   #    fig.update_xaxes(tickangle=-45)
   #    newnames = {'D':'Democrats'}
   #    fig.for_each_trace(lambda t: t.update(name = newnames[t.name]))
   #    st.plotly_chart(fig)
   
   # elif party_group == 'Both':
   #    fig = px.bar(data,x='State',color='Party',color_discrete_map={'R': 'red','D': 'blue'},width=900,height=400,labels={'count': 'Amount'})
   #    fig.update_layout(xaxis={'categoryorder':'total descending'})
   #    fig.update_xaxes(tickangle=-45)
   #    fig.update_yaxes(title=None)
   #    newnames = {'R':'Republicans','D':'Democrats'}
   #    fig.for_each_trace(lambda t: t.update(name = newnames[t.name]))
   #    st.plotly_chart(fig)

   # fig = px.bar(data,x='State',color='Party',color_discrete_map={'D': 'Blue', 'R':'Red'},title="Committee Members per Party",width=1000, height=800,barmode="group")
   # fig.update_layout(xaxis={'categoryorder':'total descending'})
   # st.plotly_chart(fig)


   # fig = px.bar(data, x='District', color='Party', color_discrete_map={'D': 'Blue', 'R':'Red'},width=1200, height=400)
   # fig.update_layout(xaxis={'categoryorder':'total descending'})
   # newnames = {'R':'Republicans','D':'Democrats'}
   # fig.for_each_trace(lambda t: t.update(name = newnames[t.name]))
   # fig.update_xaxes(tickangle=45)
   # st.plotly_chart(fig)

   # fig = px.bar(
   #    data_melt_committee,
   #    y='Committee Assignment',
   #    color='Party',
   #    color_discrete_map={'D': 'Blue', 'R':'Red'},
   #    orientation='h',
   #    title="Representatives per Party grouped by Committee",
   #    width=1200, height=400)
   # fig.update_layout(yaxis={'categoryorder':'total descending'})
   # newnames = {'R':'Republicans','D':'Democrats'}
   # st.plotly_chart(fig)

   # order = {'District':['1st','2nd','3rd','4th','5th','6th','7th','8th','9th','10th' ,'11th','12th','13th','14th','15th','16th','17th','18th','19th','20th','21st','22nd','23rd','24th','25th','26th','27th','28th','29th','30th','31st','32nd','33rd','34th','35th','36th','37th','38th','39th','40th','41st','42nd','43rd','44th','45th','46th','47th','48th','49th','50th','51st','52nd','53rd','At Large', 'Delegate','Resident Commissioner']}
   # fig = px.bar(data,x='District',color='Party',color_discrete_map={'D': 'Blue', 'R':'Red'},title="Committee Members per Party",width=1300, height=800,category_orders=order,facet_col="Party")
   # fig.update_layout(xaxis={'categoryorder':'total descending'})
   # newnames = {'R':'Republicans','D':'Democrats'}
   # fig.for_each_trace(lambda t: t.update(name = newnames[t.name])) # Interactive graph does not show up on GitHub
   # st.plotly_chart(fig)

   # fig = px.bar(data,x='District',color='Party',color_discrete_map={'D': 'Blue', 'R':'Red'},title="Committee Members per Party",width=1400, height=800,barmode="group",category_orders=order)
   # fig.update_xaxes(tickangle=45)
   # st.plotly_chart(fig)

   # st.markdown('''
   # <center>
   #    <p style="font-size:30px;">
   #       <b> Part 3/3: </b>
   #       Conclusion
   #    </p>
   # </center>
   # ''',unsafe_allow_html=True)

# ## -----------------------------------------  ------------------------------------------------------------------------ ##
# else:
#    data = pd.DataFrame({'a':range(10)})
#    url = "EXAMPLE.ORG"
#    url_split = url.replace('https://','').split('/')[0]

## ----------------------------------------- Politicos Chilenos - Camara Diputados ------------------------------------------------------------------------ ##
if projectOption[project] == 17:
   from Projects._17_BoatTrader import BoatTrader
   
   url = BoatTrader.url_main # https://www.boattrader.com/boat-dealers/
   data = BoatTrader.data
   script_1 = BoatTrader.script_1
   
   st.markdown('''
   <center>
      <img src='https://boattrader.com/static/img/tol-design/btol/bt-inc-release/boattrader-logo.png' alt="Logo">
   </center>
   ''',unsafe_allow_html=True)

   st.markdown(f'''
   <h1 style="font-size:40px;text-align:center;"> Description: </h1>
   <p style="font-size:20px;text-align:center;">
      I was asked to gather all 2400+ boat dealers and contact information for owner, sale manager, general manager and/or marketing manager listed on
         <a href="{url}"> boattrader.com</a>. 
      They wanted me to extract the Enter Name, Title, Email, Mailing Address and Phone for each dealer and position at dealership (not all applied, not all are listed),
      and to enter it into an Excel or Google Sheet (whichever I prefer).
      <br><br>
      Here is the code, website, table with data extracted, and analysis:
   </p>
   ''',unsafe_allow_html=True)
   
   with st.expander("Code Used 🐍"):
      st.code(script_1,language="python")
   with st.expander("See Website 👨🏻‍💻"):
      st.markdown(f'''<a href={url}>{url}</a>''',unsafe_allow_html=True)
      col1, col2, col3 = st.columns([1,3,1])
      with col1:
         st.write(' ')
      with col2:
         components.iframe(f"{url}", width=350, height=500, scrolling=True)
      with col3:
         st.write(' ')
   with st.expander("Data Extracted 🕸"):
      st.write("Table containing data extracted from website")
      st.download_button(
         label     =    "Download data as CSV",
         data      =    data.to_csv().encode('utf-8'),
         file_name =    'BoatTrader_dealers.csv',
         mime      =    'text/csv',)
      st.dataframe(data)
   with st.expander("Analysis 🧐"):   
      KPI1, KPI2, KPI3, KPI4 = st.columns(4)
      KPI1.metric('Number of dealers', f"{data.shape[0]}")
      KPI2.metric("Number of duplicates", f"{data[data.name.duplicated()].shape[0]}") # based on dealership name
      KPI3.metric("Dealers without phone", data[data.phone.isna()].shape[0])
      KPI4.metric("Dealers with website", data[(~data.website.isna()) & (data.name.duplicated() == False)].shape[0])
      st.write('Boat dealers by state')
      plot_state = data.groupby('state').aggregate('count').reset_index()[['state','id']].sort_values('id', ascending=False).rename(columns={"id": "count"})
      st.bar_chart(plot_state, x='state', y='count')
      state_name = data.state.value_counts().reset_index().iloc[0,0] # Florida
      state_perc = data.state.value_counts().iloc[0]
      state_rank = data.groupby('state').aggregate('count').loc['FL']['id']
      data_diff = round(state_perc / data.groupby('state').aggregate('count')['id'].mean(),1) 

      st.write(f"""Florida ({state_name}) is the state with most boat dealers with {state_perc} stores across the United States,
      it also has {data_diff} times more boat dealer than the average state amount.""")

# ---------

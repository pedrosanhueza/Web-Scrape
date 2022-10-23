
## ----------------------------------------- Import -------------------------------------------------------------------------------------- ##
import streamlit as st
import pandas as pd
from datetime import datetime, timedelta
import time
import pytz
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import plotly.express as px
from plotly.figure_factory import create_distplot


# from Projects._1_Billionaires import forbesBillionaires
# from Projects._2_BYUI_ClassCatalog import catalogBYUI
# from Projects._3_CountryCode import countryCode
# from Projects._4_FIFAWorldCup import FIFAWorldCup
# # from Projects._5_Financial Data import 
# from Projects._6_ForbesBillionaries import forbesBillionaires
# from Projects._7_ForbesUniversities import Forbes_Universities
# from Projects._8_IrvineSpectrumCenter import irvinespectrumcenter
from Projects._9_BYUI_JobBoard import BYUI_JobBoard
# from Projects._10_MutualAppFeedback import Mutual_App_Feedback
# from Projects._11_NewsCBS import cbsnews
# # from Projects._12_PoliticosChilenos import 
# from Projects._13_PoliticosEspanoles import DiputadosEspanoles
# from Projects._14_SINCAMMAGob import SINCAMMAGob
from Projects._15_BYUI_SurplusStore import SurplusStore
from Projects._16_USHouseRepresentatives import representatives
# from Projects.test import test

st.set_option('deprecation.showPyplotGlobalUse', False)

## ----------------------------------------- General Variables ----------------------------------------------------------------------------- ##

IdahoTz = pytz.timezone('US/Mountain') 
timeZoneMountain = datetime.now(IdahoTz)
currentTimeInRexburg = timeZoneMountain.strftime("%Y-%m-%d")
YesterdayTimeInRexburg = (timeZoneMountain - timedelta(1)).strftime("%Y-%m-%d")

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
   st.write('Hola!')

   data = BYUI_JobBoard.data

   # def convert_date(x,y,z):   
   #    orig_date = datetime(x,y,z)
   #    orig_date = str(orig_date)
   #    d = datetime.strptime(orig_date, '%Y-%m-%d %H:%M:%S')
   #    d = d.strftime('%m-%d-%y')
   #    return d

   # start_dates = data.startDate.dropna().replace('T',' ',regex=True)

   # start_dates_formatted = [x for x in ]

   # start_dates_formatted = [datetime.strptime(d, "%Y-%m-%d %H:%M:%S") for d in start_dates]
   # start_dates_formatted_1 = [d for d in start_dates_formatted if d > currentTimeInRexburg]
   # rand_names = range(34)

   # st.write(rand_names)



## ----------------------------------------- Class Catalog - BYUI ------------------------------------------------------------------------ ##
# elif projectOption[option] == 2:
#    data = catalogBYUI.data
#    url = catalogBYUI.url
#    url_split = url.replace('https://','').split('/')[0]

#    tab1, tab2, tab3, tab4 = st.tabs(['Overview', 'Table', 'Code', 'Analysis'])

#    with tab1:
#       st.header(option)
#       col1, col2, col3 = st.columns(3)
#       col1.metric("Classes", data.shape[0], "1.2 °F")
#       col2.metric("Subjects", data.description.nunique(), "-8%")
#       col3.metric("Humidity", "86%", "4%")

#       st.image('@Calling-Code/Projects/CatalogBYUI/CatalogBYUI.png', caption='Website page')
      
#       # f"[{url_split}]({url}) website"
#    with tab2:
#       st.header(f"Data extracted from @@@")
#       # st.header(f"Data extracted from {url_split}")
#       st.dataframe(data)
#    with tab3:
#       st.header("Code")
#    with tab4:
#       st.header("Analysis")

# ## ----------------------------------------- Billionaires ------------------------------------------------------------------------ ##
# elif projectOption[option] == 3:
#    data = countryCode.data
#    url = countryCode.url
#    url_split = url.replace('https://','').split('/')[0]

# ## ----------------------------------------- FIFA World Cup ------------------------------------------------------------------------ ##
# elif projectOption[option] == 4:
#    st.header(option)

#    data = FIFAWorldCup.data

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
   
#    url_pic = 'https://upload.wikimedia.org/wikipedia/commons/thumb/5/57/Easports_fifa_logo.svg/800px-Easports_fifa_logo.svg.png'
   
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

# ## ----------------------------------------- Job Board - BYUI ------------------------------------------------------------------------ ##
elif projectOption[option] == 9:
   
   st.markdown('''
   <p style="text-align:right;">
      Author: Pedro Sanhueza
   </p>
   
   <center>
      <h1 style="color:#214491;font-size: 90px;">
         BYU-I
         <br>
         Job Board 
      </h1>
   </center>
   
   <br>
  ''',unsafe_allow_html=True)

   data = BYUI_JobBoard.data
   
   d = str(datetime.today().strftime("%Y-%m-%d"))

   KPI1_jobs = round(1-(400/data.shape[0]),2)

   KPI1_1_max = round(1-(data.payRate.median()/data.payRate.max()),2)

   today_data = data[data.dateUpdated >= currentTimeInRexburg]

   today = today_data.shape[0]

   yesterday_data = data[data.dateUpdated == (datetime.today() - timedelta(1)).strftime("%Y-%m-%d")]

   yesterday = yesterday_data.shape[0]

   KPI1, KPI2, KPI3, KPI4 = st.columns(4)

   KPI1.metric('Jobs Published', f"{data.shape[0]}")

   KPI2.metric("Departments Recluting", f"{data.departmentName.nunique()}")

   KPI3.metric("Jobs Posted Today",today)

   KPI4.metric("Highest Pay Rate Job", f"${data.payRate.max()}")

   st.markdown('''
   <br>
   <p style="font-size:40px;text-align:center;color:#4F9ACF;">
      Highest Paid Jobs
   </p>
   <br>
   ''',unsafe_allow_html=True)

   Njobs = st.slider('Select a range of jobs', 1, 10, 5)

   data_topPayRate = data.sort_values('payRate', ascending=False).head(Njobs)[['title','payRate','departmentName','managerName','URL']]
   
   data_topPayRate.columns = ['Job Title','Hourly Wage','Department','Employer','Application Link']

   st.dataframe(data_topPayRate.reset_index().drop('index',axis=1))

   if today > 0:

      st.markdown(f'''
      <br>
      <p style="font-size:40px;text-align:center;color:#4F9ACF;">
         Jobs Posted Today
      </p>
      <p style="text-align:center;color:#4F9ACF;">
         {currentTimeInRexburg}
      </p>
      <br>
      ''',unsafe_allow_html=True)

      st.dataframe(today_data[['title','payRate','departmentName','managerName','URL']].sort_values('payRate',ascending=False))
   elif yesterday > 0:
      st.markdown(f'''
      <br>
      <p style="font-size:40px;text-align:center;color:#4F9ACF;">
         Jobs Posted Yesterday
      </p>
      <p style="text-align:center;color:#4F9ACF;">
         {YesterdayTimeInRexburg}
      </p>
      <br>
      ''',unsafe_allow_html=True)

      st.dataframe(yesterday_data[['title','payRate','departmentName','managerName','URL']].sort_values('payRate',ascending=False))

   st.markdown('''
   <br>
   <p style="font-size:40px;text-align:center;color:#4F9ACF;">
      Pay Rate Distribution
   </p>
   <br>
   ''',unsafe_allow_html=True)

   col1, col2 = st.columns([4,1])

   with col2:
      job_type = st.radio("Job Type", ('All','Online','On-Campus'))
      
      if job_type == 'Online':
         data_isOnline = data[data.isOnline == True]
      elif job_type == 'On-Campus':
         data_isOnline = data[data.isOnline == False]
      else:
         data_isOnline = data.copy()

   with col1:   
      sns.kdeplot(data_isOnline.payRate, shade=True, color="#214491", bw=0.8, alpha=0.5, cut=0)
      fig1 = plt.show()
      st.pyplot(fig1)

   tab1, tab2 = st.tabs(['Data','Code'])

   with tab1:
      columns_ls = st.multiselect(
      '',
      data.columns,
      ['title', 'payRate','managerName'])

      st.dataframe(data[columns_ls])

      @st.cache
      def convert_df(df):
         # IMPORTANT: Cache the conversion to prevent computation on every rerun
         return df.to_csv().encode('utf-8')

      csv = convert_df(data)

      file_name = 'BYUI_jobBoard_' + str(time.strftime("%Y-%m-%d"))

      st.download_button(
         label = "Download data as CSV",
         data = csv,
         file_name = file_name,
         mime = 'text/csv')

   with tab2:

      st.markdown(f'''
      <br>
      <p style="font-size:20px;text-align:center;color:#4F9ACF;">
         🐍 Source Code
      </p>
      <a style="color:#4F9ACF; padding:7px 10px;"
         target="_blank" 
         href = 'https://github.com/pedrosanhueza/Web_Scrape/blob/main/BYUI_JobBoard/Job_board-Code/API-call-JobBoard.ipynb'>
         GitHub Repository
      </a>
      <br>
      ''',unsafe_allow_html=True)

      st.code(BYUI_JobBoard.script1, language='python')
   
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
   



# ## -----------------------------------------  ------------------------------------------------------------------------ ##
elif projectOption[option] == 15:
   data = SurplusStore.data


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

   # names = data['Condition'].value_counts().reset_index()['index']

   # values = data['Condition'].value_counts().reset_index()['Condition']
   
   st.line_chart(data[['Condition']])

# ## -----------------------------------------  ------------------------------------------------------------------------ ##
elif projectOption[option] == 16: 
   data = representatives.data
   
   st.dataframe(data)

   party_group = st.radio("Representative Members by State",('Both','Republicans','Democrats'), horizontal=True)

   if party_group == 'Republicans':
      fig = px.bar(data[data.Party=='R'],x='State',color='Party',color_discrete_map={'R': 'red'},width=900,height=400,labels={'count': 'Amount'})
      fig.update_layout(xaxis={'categoryorder':'total descending'})
      fig.update_xaxes(tickangle=-55)
      newnames = {'R':'Republicans'}
      fig.for_each_trace(lambda t: t.update(name = newnames[t.name]))
      st.plotly_chart(fig)

   elif party_group == 'Democrats':
      fig = px.bar(data[data.Party=='D'],x='State',color='Party',color_discrete_map={'D': 'Blue'},width=900,height=400,labels={'count': 'Amount'})
      fig.update_layout(xaxis={'categoryorder':'total descending'})
      fig.update_xaxes(tickangle=-45)
      newnames = {'D':'Democrats'}
      fig.for_each_trace(lambda t: t.update(name = newnames[t.name]))
      st.plotly_chart(fig)
   
   elif party_group == 'Both':
      fig = px.bar(data,y='State',color='Party',color_discrete_map={'R': 'red','D': 'blue'},width=800,height=950,labels={'count': 'Amount'},orientation='h')
      fig.update_layout(yaxis={'categoryorder':'total ascending'})
      fig.update_xaxes(tickangle=-45)
      fig.update_yaxes(title=None)
      newnames = {'R':'Republicans','D':'Democrats'}
      fig.for_each_trace(lambda t: t.update(name = newnames[t.name]))
      st.plotly_chart(fig)



   fig = px.bar(data,x='State',color='Party',color_discrete_map={'D': 'Blue', 'R':'Red'},title="Committee Members per Party",width=1000, height=800,barmode="group")
   fig.update_layout(xaxis={'categoryorder':'total descending'})
   st.plotly_chart(fig)

   newnames = {'R':'Republicans','D':'Democrats'}
   fig = px.pie(data['Party'].replace(newnames),names='Party',color='Party',color_discrete_map={'Republicans':'Red','Democrats':'Blue'})
   fig.update_traces(textfont_size=22,textinfo='percent+value')
   st.plotly_chart(fig)

   fig = px.bar(data, x='District', color='Party', color_discrete_map={'D': 'Blue', 'R':'Red'},width=1200, height=400)
   fig.update_layout(xaxis={'categoryorder':'total descending'})
   newnames = {'R':'Republicans','D':'Democrats'}
   fig.for_each_trace(lambda t: t.update(name = newnames[t.name]))
   fig.update_xaxes(tickangle=45)
   st.plotly_chart(fig)

   data_melt_committee = data.copy()
   data_melt_committee[[0,1,2,3,4,5]] = data['Committee Assignment'].str.split('|',expand=True)
   data_melt_committee.drop('Committee Assignment',axis=1, inplace=True)
   data_melt_committee = data_melt_committee.melt(id_vars=['District','Name','Party','Office Room','Phone','State'],value_name='Committee Assignment')
   data_melt_committee = data_melt_committee[~data_melt_committee['Committee Assignment'].isnull()].drop('variable',axis=1)
   fig = px.bar(
      data_melt_committee,
      y='Committee Assignment',
      color='Party',
      color_discrete_map={'D': 'Blue', 'R':'Red'},
      orientation='h',
      title="Representatives per Party grouped by Committee",
      width=1200, height=400)
   fig.update_layout(yaxis={'categoryorder':'total descending'})
   newnames = {'R':'Republicans','D':'Democrats'}
   st.plotly_chart(fig)

   order = {'District':['1st','2nd','3rd','4th','5th','6th','7th','8th','9th','10th' ,'11th','12th','13th','14th','15th','16th','17th','18th','19th','20th','21st','22nd','23rd','24th','25th','26th','27th','28th','29th','30th','31st','32nd','33rd','34th','35th','36th','37th','38th','39th','40th','41st','42nd','43rd','44th','45th','46th','47th','48th','49th','50th','51st','52nd','53rd','At Large', 'Delegate','Resident Commissioner']}
   fig = px.bar(data,x='District',color='Party',color_discrete_map={'D': 'Blue', 'R':'Red'},title="Committee Members per Party",width=1300, height=800,category_orders=order,facet_col="Party")
   fig.update_layout(xaxis={'categoryorder':'total descending'})
   newnames = {'R':'Republicans','D':'Democrats'}
   fig.for_each_trace(lambda t: t.update(name = newnames[t.name])) # Interactive graph does not show up on GitHub
   st.plotly_chart(fig)

   fig = px.bar(data,x='District',color='Party',color_discrete_map={'D': 'Blue', 'R':'Red'},title="Committee Members per Party",width=1400, height=800,barmode="group",category_orders=order)
   fig.update_xaxes(tickangle=45)
   st.plotly_chart(fig)

# ## -----------------------------------------  ------------------------------------------------------------------------ ##
# else:
#    data = pd.DataFrame({'a':range(10)})
#    url = "EXAMPLE.ORG"
#    url_split = url.replace('https://','').split('/')[0]


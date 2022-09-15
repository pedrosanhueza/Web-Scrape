
# ------------------------|---------|------------------------ #
# ------------------------|JOB BOARD|------------------------ #
# ------------------------|---------|------------------------ #


# ------------------------ LIBRARIES ------------------------------------------------------------------------------------------------

import requests
import pandas as pd
import streamlit as st
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
import time

# ------------------------ STREAMLIT ------------------------------------------------------------------------------------------------

'# BYU - Idaho student employment'

# ------------------------ REQUESTS ------------------------------------------------------------------------------------------------

response = requests.get('https://web.byui.edu/studentemployment/api/jobs')

data_json = response.json()

data_raw = pd.DataFrame(data_json)

# ------------------------ WRANGLE ------------------------------------------------------------------------------------------------

data = data_raw.copy()

col_dates = ['dateUpdated','startDate','endDate','beginningDate','recruitingStartDate']

data[col_dates] = data[col_dates].astype('datetime64[ns]')

data.dateUpdated = data.dateUpdated.apply(lambda x: datetime.strftime(x, "%Y-%m-%d"))

data['URL'] = data.jobID.apply(lambda x: f'https://web.byui.edu/StudentEmployment/job/{x}')

columns_to_drop = [
    'jobID', # not needed for EDA
    'description', # not needed for EDA
    'summary', # not needed for EDA
    'displayJob', # single boolean
    # 'dateUpdated', # not needed for display
    # 'startDate',
    # 'endDate', # not needed for display
    'approximateHoursPerWeek', # not consistent
    'positionsAllocated', # not relevant
    'positionsAvailble', # not relevant
    # 'workSchedule', # not needed for EDA
    # 'recruitingStartDate', # not relevant
    'requireResume', # not relevant
    'limitApplicants', # not relevant
    'limitNumber', # not relevant
    'applicants', # empty
    'jobQuestions', # empty
    'isOnline', # not accurate
    'allowOnline', # not accurate
    'jobMajors' # not relevant
    ]

data.drop(columns_to_drop, axis=1, inplace=True)

# data['description'] = data['description'].apply(lambda x: [p.text.strip() for p in BeautifulSoup(x).find_all('p') if p.text.strip() != ''])

# ------------------------ STREAMLIT SIDE BAR ------------------------------------------------------------------------------------------------

st.sidebar.write('# FILTERS')

date_input = st.sidebar.date_input("Jobs posted on",datetime.today())

d = str(date_input.strftime("%Y-%m-%d"))

# ------------------------ STREAMLIT KPI GENERAL ------------------------------------------------------------------------------------------------

'## General KPI\'s'

KPI1_jobs = round(1-(400/data.shape[0]),2)

KPI1_1_max = round(1-(data.payRate.median()/data.payRate.max()),2)

jobs_not_online = data[~data.title.str.contains('Online')].shape[0]

KPI1,KPI1_1,KPI2 = st.columns(3)

KPI1.metric("Amount of Jobs", f"{data.shape[0]}")

KPI1_1.metric("Highest Pay Rate Job", f"${data.payRate.max()}")

KPI2.metric("Managers Recluting", f"{data.managerName.nunique()}")

today = data[data.dateUpdated == time.strftime("%Y-%m-%d")].shape[0]

yesterday = data[data.dateUpdated == (datetime.today() - timedelta(1)).strftime("%Y-%m-%d")].shape[0]

KPI3, KPI4, KPI_K = st.columns(3)

KPI3.metric("Departments hiring", f"{data.departmentName.nunique()}")

try:
    KPI4.metric("Jobs posted today",today, f'{round((today/yesterday)-1,2)}% of yesterday')
except:
    KPI4.metric("Jobs posted today",today, f'0% of yesterday')

KPI_K.metric("Jobs not Online", f"{jobs_not_online}")

# ------------------------ STREAMLIT  ----------------------------------------------------)--------------------------------------------

f"## Jobs posted today ({date_input.strftime('%b %d, %Y')})"

f'Jobs posted: {data[data.dateUpdated == d].shape[0]}'

st.table(data[data.dateUpdated == d][['title','payRate','departmentName','URL']])


"## Highest 3 paid jobs:"

J_data = data.sort_values('payRate',ascending=False).head(3)

title_1 = J_data['title'].iloc[0]
title_2 = J_data['title'].iloc[1]
title_3 = J_data['title'].iloc[2]

rate_1 = J_data['payRate'].iloc[0]
rate_2 = J_data['payRate'].iloc[1]
rate_3 = J_data['payRate'].iloc[2]

url_1 = J_data['URL'].iloc[0]
url_2 = J_data['URL'].iloc[1]
url_3 = J_data['URL'].iloc[2]

J1,J2,J3 = st.columns(3)

J1.metric(title_1, rate_1, url_1)
J2.metric('Title', J_data['payRate'].iloc[1],'[apply](https://share.streamlit.io/mesmith027/streamlit_webapps/main/MC_pi/streamlit_app.py)')
J3.metric('Title', J_data['payRate'].iloc[2],'[apply](https://share.streamlit.io/mesmith027/streamlit_webapps/main/MC_pi/streamlit_app.py)')

# ------------------------ STREAMLIT TABLE ------------------------------------------------------------------------------------------------

st.dataframe(data)

# ------------------------ STREAMLIT GRAPH ------------------------------------------------------------------------------------------------

Chart_option = st.selectbox(
     'what would you like to see?',
     ('Pay Rate Bar Char', 'Specific Job', 'Mobile phone'))

df1 = data.payRate.value_counts().reset_index().rename(columns={"index": "Hourly Pay", "payRate": "Amount of Jobs"})

if Chart_option == 'Pay Rate Bar Char':
    st.bar_chart(
    df1,
    y='Amount of Jobs',
    x='Hourly Pay'
    )

if Chart_option == 'Specific Job':

    job_title = st.text_input('Job title:', 'Enter job title here')

    df2 = data[data.title == job_title].iloc[0]

    f'Title: \t\t {df2[0]}'
    f'Department: {df2[1]}'
    # f'Description: {df2[2][0]}'
    f'Employer: {df2[3]}'
    f'Pay Rate Hourly: {df2[4]}'
    f'Work Schedule: {df2[5]}'

df2 = data.endDate.value_counts().reset_index().rename(columns={"index": "endDate", "endDate": "Amount of Jobs"})
st.bar_chart(
df2,
y='Amount of Jobs',
x='endDate'
)

# TO DO

# I WANNA SEE TOP 3 HIGEST PY JOBS AND THEIR DETILS IN A ORGANIZED MANNER
# GRAPH OF JOBS POSTED OVERTIME -- WHEN JOBS GET POST THE MOST
# AVERAGE PAY RATE, VALUE COUNT

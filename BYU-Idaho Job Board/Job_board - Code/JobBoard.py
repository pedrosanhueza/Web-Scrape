
# ------------------------ LIBRARIES ------------------------------------------------------------------------------------------------

import requests
import pandas as pd
import streamlit as st
from bs4 import BeautifulSoup
import numpy as np

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

data['URL'] = data.jobID.apply(lambda x: f'https://web.byui.edu/StudentEmployment/job/{x}')

columns_to_drop = [
    'jobID', # not needed for EDA
    # 'description', # not needed for EDA
    'summary', # not needed for EDA
    'displayJob', # single boolean
    'dateUpdated', # not needed for display
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

data['description'] = data['description'].apply(lambda x: [p.text.strip() for p in BeautifulSoup(x).find_all('p') if p.text.strip() != ''])

# ------------------------ STREAMLIT SIDE BAR ------------------------------------------------------------------------------------------------

st.sidebar.write('# FILTERS')

# ------------------------ STREAMLIT KPI GENERAL ------------------------------------------------------------------------------------------------

'## General KPI\'s'

KPI1_jobs = round(1-(400/data.shape[0]),2)


KPI1_1_max = round(1-(data.payRate.median()/data.payRate.max()),2)

jobs_not_online = data[~data.title.str.contains('Online')].shape[0]

KPI1,KPI1_1,KPI_K,KPI2, KPI3 = st.columns(5)

KPI1.metric("Amount of Jobs", f"{data.shape[0]}")

KPI1_1.metric("Highest Pay Rate Job", f"${data.payRate.max()}")

KPI_K.metric("Jobs not Online", f"{jobs_not_online}")

KPI2.metric("Managers Recluting", f"{data.managerName.nunique()}")

KPI3.metric("Departments", f"{data.departmentName.nunique()}")

st.dataframe(data)

Chart_option = st.selectbox(
     'How would you like to be contacted?',
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
    f'Description: {df2[2][0]}'
    f'Employer: {df2[3]}'
    f'Pay Rate Hourly: {df2[4]}'
    f'Work Schedule: {df2[5]}'

df2 = data.endDate.value_counts().reset_index().rename(columns={"index": "endDate", "endDate": "Amount of Jobs"})
st.bar_chart(
df2,
y='Amount of Jobs',
x='endDate'
)
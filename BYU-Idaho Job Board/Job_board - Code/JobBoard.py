
# ------------------------ LIBRARIES ------------------------------------------------------------------------------------------------

import requests
import pandas as pd
import streamlit as st
from bs4 import BeautifulSoup
from datetime import date

# ------------------------ STREAMLIT ------------------------------------------------------------------------------------------------

'# BYU - Idaho student employment live web scraper'

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
    'startDate',
    'endDate', # not needed for display
    'approximateHoursPerWeek', # not consistent
    'positionsAllocated', # not relevant
    'positionsAvailble', # not relevant
    # 'workSchedule', # not needed for EDA
    'recruitingStartDate', # not relevant
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

# side bar slider
min = float(data.payRate.min())
max = float(data.payRate.max())
step = 0.01
payRate = st.sidebar.slider(f'Pay Rate Range', min, max, step=step)

# Using object multiselect
departments = st.sidebar.multiselect(
    "Departments",
    list(data.departmentName.unique()),
    list(data.departmentName.unique())
)

# Using "with" notation
with st.sidebar:
    add_radio = st.radio(
        "Choose a shipping method",
        ("Standard (5-15 days)", "Express (2-5 days)")
    )

# ------------------------ STREAMLIT KPI GENERAL ------------------------------------------------------------------------------------------------

'## General KPI\'s'

KPI1_jobs = round(1-(400/data.shape[0]),2)

KPI1_1_max = round(1-(data.payRate.median()/data.payRate.max()),2)

jobs_not_online = data[~data.title.str.contains('Online')].shape[0]

KPI1,KPI1_1,KPI_K,KPI2, KPI3 = st.columns(5)
KPI1.metric("Amount of Jobs", f"{data.shape[0]}", f"{KPI1_jobs}%")
KPI1_1.metric("Highest Pay Rate Job", f"${data.payRate.max()}", f"{KPI1_1_max}%")
KPI_K.metric("Jobs not Online", f"{jobs_not_online}", f"{data.shape[0] / jobs_not_online}%")
KPI2.metric("Managers Recluting", f"{data.managerName.nunique()}", "-8%")
KPI3.metric("Departments", f"{data.departmentName.nunique()}", "4%")

# ------------------------ STREAMLIT KPI FILTERED ------------------------------------------------------------------------------------------------

col_order = ['title', 'departmentName', 'payRate', 'managerName', 'workSchedule', 'beginningDate', 'description','URL']

# filter Pay Rate
data_filter = data[data['payRate']>payRate][col_order]

# filter Department
data_filter = data_filter[data_filter.departmentName.isin(departments)]

KPI1_f = round(1-(400/data.shape[0]),2)

KPI1_1_max = round(1-(data.payRate.median()/data.payRate.max()),2)

jobs_not_online = data[~data.title.str.contains('Online')].shape[0]

f'''### Filtered KPI\'s (payRate {payRate})'''

KPI1,KPI1_1,KPI_K,KPI2, KPI3 = st.columns(5)
KPI1.metric("Amount of Jobs", f"{data_filter.shape[0]}", f"{KPI1_jobs}%")
KPI1_1.metric("Highest Pay Rate Job", f"${data_filter.payRate.max()}", f"{KPI1_1_max}%")
KPI_K.metric("Jobs not Online", f"{jobs_not_online}", f"{data_filter.shape[0] / jobs_not_online}%")
KPI2.metric("Managers Recluting", f"{data_filter.managerName.nunique()}", "-8%")
KPI3.metric("Departments", f"{data_filter.departmentName.nunique()}", "4%")

st.dataframe(data_filter)
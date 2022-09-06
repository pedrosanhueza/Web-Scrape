
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

columns_to_drop = [
    'jobID', # not needed for EDA
    # 'description', # not needed for EDA
    'summary', # not needed for EDA
    'displayJob', # single boolean
    'dateUpdated', # not needed for display
    # 'startDate',
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

# ------------------------ STREAMLIT ------------------------------------------------------------------------------------------------


col1, col2, col3 = st.columns(3)
col1.metric("Jobs", f"{data.shape[0]}", "1.2 °F")
col2.metric("Managers recluting", "9 mph", "-8%")
col3.metric("Departments recluting", "86%", "4%")

f'''

#### Quick overview:

Jobs posted: {data.shape[0]}

Jobs that are not 'Online', 'TA', nor 'custodial': {data[~data.title.str.contains('TA|Custodian|Online')].shape[0]}

Managers recluting: {data.managerName.nunique()}

Departments recluting: {data.departmentName.nunique()}

'''

'#### Data filtered:'

min = float(data.payRate.min())
max = float(data.payRate.max())
step = 0.01

payRate = st.slider(f'Pay Rate minimum?', min, max, step=step)

col_order = ['title', 'departmentName', 'payRate', 'managerName','startDate', 'workSchedule', 'beginningDate', 'description']

data_KPI = data[data['payRate']>payRate][col_order]

f'''

Jobs posted: {data_KPI.shape[0]}

Jobs that are not 'Online', 'TA', nor 'custodial': {data_KPI[~data_KPI.title.str.contains('TA|Custodian|Online')].shape[0]}

Managers recluting: {data_KPI.managerName.nunique()}

Departments recluting: {data_KPI.departmentName.nunique()}

'''

data_KPI
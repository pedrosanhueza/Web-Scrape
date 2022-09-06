import requests
import pandas as pd
import streamlit as st
from bs4 import BeautifulSoup
from datetime import date

st.write('''# BYU - Idaho student employment live web scraper''')

response = requests.get('https://web.byui.edu/studentemployment/api/jobs')

data_json = response.json()

data_raw = pd.DataFrame(data_json)

data = data_raw.copy()

col_dates = ['dateUpdated','startDate','endDate','beginningDate','recruitingStartDate']

data[col_dates] = data[col_dates].astype('datetime64[ns]')

columns_to_drop = [
    'jobID', # not needed for EDA
    # 'description', # not needed for EDA
    'summary', # not needed for EDA
    'displayJob', # single boolean
    'dateUpdated','startDate','endDate', # not needed for display
    'approximateHoursPerWeek', # not consistent
    'positionsAllocated', # not relevant
    'positionsAvailble', # not relevant
    # 'workSchedule', # not needed for EDA
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

st.write(f'''
#### As of {date.today().strftime("%B %d, %Y")} there are {data.shape[0]} jobs posted in [BYU-I Student Employment](https://web.byui.edu/StudentEmployment)
#### Quick overview:
''')

st.dataframe(data)

st.write(f'''There are {data[~data.title.str.contains('TA|Custodian|Online')].shape[0]} jobs that are not Online, TA, not custodial''')

st.dataframe(data[~data.title.str.contains('TA|Custodian|Online')].sort_values('payRate', ascending=False)[['title','payRate','workSchedule']])
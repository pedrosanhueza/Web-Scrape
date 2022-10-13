import requests
import pandas as pd

response = requests.get('https://web.byui.edu/studentemployment/api/jobs')

data_json = response.json()

data = pd.DataFrame(data_json)

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


import streamlit as st
import requests
import pandas as pd

response = requests.get('https://www.forbes.com/forbesapi/org/top-colleges/2021/position/true.json?limit=1000&fields=organizationName,academics,state,financialAid,rank,medianBaseSalary,campusSetting,studentPopulation,organization,description')

responseObject = response.json()

responseData = responseObject['organizationList']['organizationsLists']

data_main = pd.DataFrame(responseData)

# ----------------------------- Adding 'organization' to main table -----------------------------

# add organization
organization = [ x['organization'] for x in responseData]
data_main = pd.concat([data_main, pd.DataFrame(organization)], axis=1)
#### Add single 'Primary_Key' column to main table
# add naturalId column
data_main['Primary_Key'] = [ x['organization']['naturalId'].split('/')[-1] for x in responseData]

# ----------------------------- Adding 'organization/geoLocation' to main table -----------------------------

# add geoLocation columns
rows = []
for organizationsLists in responseData:
    row = {}    
    # row['Primary_Key'] = organizationsLists['organization']['naturalId'].split('/')[-1]
    try:
        row['latitude'] = organizationsLists['organization']['geoLocation']['latitude']
    except:
        pass
    try:
        row['longitude']= organizationsLists['organization']['geoLocation']['longitude']
    except:
        pass
    rows.append(row)
data_main = pd.concat([data_main, pd.DataFrame(rows)], axis=1)
#### Adding 'Academics' to main table
academics = [ # items in the 'academics' key to be unpacked
    'attendanceStatus',
    'firstToSecondYearRetention',
    'overallGraduationRates',
    'enrollmentByGender',
    'graduationRateByGender',
    'enrollmentByRace',
    'graduationRateByRace']

def restructure(list_of_dictionaries,name): # change the shape of the json
    row = {}
    for item in list_of_dictionaries:
        key_value = [value for key,value in item.items()]
        key_name = name + '_' + key_value[0]
        row[key_name] = key_value[1]
    return row

def dataFrame_of_Item(item): # build a data frame from all json's 
    list_of_rows = []
    for organization in responseData:
        # create reshaped json
        graduationRateByRace = restructure(organization['academics'][item],item)
        # add primary_key number
        # graduationRateByRace['PrimaryKey'] = organization['organization']['naturalId'].split('/')[-1]
        # append to list
        list_of_rows.append(graduationRateByRace)
    return pd.DataFrame(list_of_rows)

# add date frames to main data
df_ls = []

for item in academics:
    df_ls.append(dataFrame_of_Item(item))

academics_unpacked = pd.concat(df_ls, axis=1)

data_main = pd.concat([data_main,academics_unpacked], axis=1)


# ----------------------------- Adding 'organization/socialNetworks' to main table -----------------------------

def restructure(list_of_dictionaries): # input: list of dictionaries | output: structured dictionary
    row = {}
    for item in list_of_dictionaries:
        key_value = [value for key,value in item.items()]
        key_name =key_value[0]
        row[key_name] = key_value[1]
    return row

def dataFrame_of_Item(col_name,item,TF): # input: name of dict to unpack | output: data frame
    list_of_rows = []
    for organization in responseData:
        # create json
        dictionary = {}
        try:
            # create reshaped json
            dictionary = dictionary | restructure(organization[col_name][item])
        except:
            pass
        # add primary_key number
        if TF:
            dictionary['Primary_Key'] = organization['organization']['naturalId'].split('/')[-1]
        # append to list
        list_of_rows.append(dictionary)
    return pd.DataFrame(list_of_rows)

df_socialNetworks = dataFrame_of_Item('organization','socialNetworks',True)

data_main = data_main.merge(df_socialNetworks, on='Primary_Key')

# ----------------------------- Adding 'financialAid' to main table -----------------------------

financialAid = [
    'grantAidByType',
    'avgGrantAidByType',
    'loansByType',
    'avgLoansByType']

def restructure(list_of_dictionaries): # input: list of dictionaries | output: structured dictionary
    row = {}
    for item in list_of_dictionaries:
        key_value = [value for key,value in item.items()]
        key_name =key_value[0]
        row[key_name] = key_value[1]
    return row

def dataFrame_of_Item(col_name,item,TF): # input: name of dict to unpack | output: data frame
    list_of_rows = []
    for organization in responseData:
        # create json
        dictionary = {}
        try:
            # create reshaped json
            dictionary = dictionary | restructure(organization[col_name][item])
        except:
            pass
        # add primary_key number
        if TF:
            dictionary['Primary_Key'] = organization['organization']['naturalId'].split('/')[-1]
        # append to list
        list_of_rows.append(dictionary)
    return pd.DataFrame(list_of_rows)

# add date frames to main data
df_ls = []

for item in financialAid:
    df_ls.append(dataFrame_of_Item('financialAid',item,True))

financialAid_unpacked = pd.concat(df_ls, axis=1)

financialAid_unpacked = financialAid_unpacked.loc[:, ~financialAid_unpacked.columns.duplicated()]

data_main = data_main.merge(financialAid_unpacked)

data_main = data_main.loc[:, ~data_main.columns.duplicated()]

drop_columns = ['organization','academics','financialAid','listImages','geoLocation','visible','relatedVisible','imageExists','socialNetworks','collegeMedia']

data_main.drop(drop_columns, axis=1, inplace=True)


# st.write('Hello')

st.map(data=data_main)

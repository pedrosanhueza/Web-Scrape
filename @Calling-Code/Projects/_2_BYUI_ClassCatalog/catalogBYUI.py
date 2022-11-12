# catalogBYUI

import requests
import pandas as pd

url_display = 'https://www.byui.edu/catalog#/courses'

url = 'https://byui.kuali.co/api/v1/catalog/courses/6102e778ef84b869ba4eb375?q='

response = requests.get(url)

responseObject = response.json()

df = pd.DataFrame(responseObject)

df = pd.concat([df, df.subjectCode.apply(pd.Series)], axis=1).drop(['subjectCode','__passedCatalogQuery','_score'], axis=1)

df.columns = [
    'catalogCourseId',
    'dateStart',
    'pid',
    'id',
    'title',
    'catalogActivationDate',
    'name',
    'description',
    'subjectCode-id',
    'linkedGroup'
]

data = df

# ----------------------- TEST -----------------------

print(data.columns)
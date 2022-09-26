# catalogBYUI

import requests
import pandas as pd

response = requests.get('https://byui.kuali.co/api/v1/catalog/courses/6102e778ef84b869ba4eb375?q=')

responseObject = response.json()

df = pd.DataFrame(responseObject)

df = pd.concat([df, df.subjectCode.apply(pd.Series)], axis=1).drop(['subjectCode','__passedCatalogQuery','_score'], axis=1)

data = df
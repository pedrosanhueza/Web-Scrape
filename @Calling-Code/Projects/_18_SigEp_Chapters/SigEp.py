import requests

import pandas as pd

url_main = 'https://sigep.org/'

# headers of this particular server
headers = {'user-agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36"}

# url with hrx dat found in network inspection
url = 'https://sigep.org/wp-admin/admin-ajax.php?action=wp_ajax_ninja_tables_public_action&table_id=18473&target_action=get-all-data&default_sorting=old_first&ninja_table_public_nonce=2b4d3aac4d'

# store response from server into a variable
response = requests.get(url,headers=headers)

# parse response data from raw response to json
response_object = response.json()

# from list of dictionary to panel data
data = pd.DataFrame(response_object)

# Select particular columns
data = data[['dyadinstitutionalid','chapterpresidentname','chapterpresidentemail','avcpresidentname','avcpresidentemail']]

# Change all columns name
data.set_axis(['instution','presidentname','presidentemail','vcpresidentname','vcpresidentemail'], axis=1, copy=True)

# ---------------- Script_1 ----------------

script_1 = '''
import requests

import pandas as pd

# headers of this particular server
headers = {'user-agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36"}

# url with hrx dat found in network inspection
url = 'https://sigep.org/wp-admin/admin-ajax.php?action=wp_ajax_ninja_tables_public_action&table_id=18473&target_action=get-all-data&default_sorting=old_first&ninja_table_public_nonce=2b4d3aac4d'

# store response from server into a variable
response = requests.get(url,headers=headers)

# parse response data from raw response to json
response_object = response.json()

# from list of dictionary to panel data
data = pd.DataFrame(response_object)

# Select particular columns
data = data[['dyadinstitutionalid','chapterpresidentname','chapterpresidentemail','avcpresidentname','avcpresidentemail']]

# Change all columns name
data.set_axis(['instution','presidentname','presidentemail','vcpresidentname','vcpresidentemail'], axis=1, copy=True)
'''
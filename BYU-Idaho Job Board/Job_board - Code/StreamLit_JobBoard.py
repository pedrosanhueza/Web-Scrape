import streamlit as st
import requests
import pandas as pd

response = requests.get('https://web.byui.edu/studentemployment/api/jobs')

data_json = response.json()

data = pd.DataFrame(data_json)

st.dataframe(data)
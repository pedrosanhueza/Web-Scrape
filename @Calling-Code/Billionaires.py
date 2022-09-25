import streamlit as st
import pandas as pd


st.write('Showing Billionaires Code here!')

data = pd.DataFrame([{'A':1}])

class B:
  def __init__(self, data, url):
    self.data = st.dataframe(data)
    self.url = 'https://www.forbes.com/billionaires/'

# st.dataFrame(
#     pd.DateFrame({'a':1})
# )
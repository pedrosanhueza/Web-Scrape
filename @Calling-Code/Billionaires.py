import streamlit as st
import pandas as pd

data = pd.DataFrame([{'A':1}])

def dataFr():
    st.write('Text inside Bill function')
    st.dataframe(data)
    st.write('END Bill function')
import streamlit as st
import pandas as pd


st.write('Showing Billionaires Code here!')

data = pd.DataFrame([{'A':1}])

def Bill(data):
    st.dataframe(data)
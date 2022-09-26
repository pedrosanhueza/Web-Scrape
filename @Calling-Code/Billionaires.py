import streamlit as st
import pandas as pd

data = pd.DataFrame([{'A':1}])

def tableFrame():
    return st.dataframe(data)

name = 'Steve Jobs'


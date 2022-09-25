# import streamlit as st
import pandas as pd

data = pd.DataFrame([{'A':1}])

def tableFrame():
    
    df = st.dataframe(data)
    
    return df
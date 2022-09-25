import streamlit as st
import pandas as pd

st.write('Showing Billionaires Code here!')

st.dataframe(pd.DataFrame([{'A':1}]))

# st.dataFrame(
#     pd.DateFrame({'a':1})
# )
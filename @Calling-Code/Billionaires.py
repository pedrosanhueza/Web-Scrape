import streamlit as st
import pandas as pd

data = pd.DataFrame([{'A':1}])

def tableFrame():
    return st.dataframe(data)

name = 'Steve Jobs'

def maindata():
    class Person:
        def __init__(self, name, age):
            self.name = name
            self.age = age

        p1 = Person("John", 36)

        print(p1.name)
        print(p1.age)
        
    return Person
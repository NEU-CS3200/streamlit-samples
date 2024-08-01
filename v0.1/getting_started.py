# First Streamlit App!!
import streamlit as st
import pandas as pd

# function to create a sample data frame and display it
def first_app():
    st.write("# CS 3200 Streamlit Super Simple Example")
    st.write("Here's our first attempt at using a dataframe to create a table:")
    st.write(pd.DataFrame({
        'variable01': [1, 2, 3, 4],
        'variable02': [10, 20, 30, 40]
    }))

# Call the first_app() function
first_app()
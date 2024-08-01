# First Streamlit App!!

import streamlit as st
import pandas as pd
import numpy as np
import time


# function to create a sample data frame and display it
def page01():
    st.sidebar.markdown("## Check and Select")
    st.write("## Here's a checkbox to control showing some data!")
    if st.checkbox('Show dataframe'):
        chart_data = pd.DataFrame(
        np.random.randn(20, 3),
        columns=['a', 'b', 'c'])

        chart_data

    st.write("## Here's a select (dropdown) widget!")
    df = pd.DataFrame({
        'first column': [1, 2, 3, 4],
        'second column': [10, 20, 30, 40]
    })

    option = st.selectbox(
        'Which number do you like best?',
        df['first column'])

    'You selected: ', option


# Call the first_app() function
page01()
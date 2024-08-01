# First Streamlit App!!

import streamlit as st
import pandas as pd
import numpy as np
import time


# function to create a sample data frame and display it
def level03():

    st.write("# So you want to get input from the USER???")
    st.write("Use Widgets to get user input... ")

    st.write("## Here's a slider to do some math!")
    x = st.slider('x')  # 👈 this is a widget
    st.write('## ', x, 'squared is', x * x)

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

    st.write("## You want a progress bar? No Problem!")
    st.write('Starting a long computation...')

    # Add a placeholder
    latest_iteration = st.empty()
    bar = st.progress(0)

    for i in range(100):
    # Update the progress bar with each iteration.
        latest_iteration.text(f'Iteration {i+1}')
        bar.progress(i + 1)
        time.sleep(0.1)

    st.write('...and now we\'re done!')


# Call the first_app() function
level03()
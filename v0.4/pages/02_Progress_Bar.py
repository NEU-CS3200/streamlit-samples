# First Streamlit App!!

import streamlit as st
import pandas as pd
import numpy as np
import time


# function to create a sample data frame and display it
def page02():
    st.sidebar.markdown("## Progress Bar")
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
page02()
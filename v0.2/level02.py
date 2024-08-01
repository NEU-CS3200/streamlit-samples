# First Streamlit App!!

import streamlit as st
import pandas as pd
import numpy as np

# function to create a sample data frame and display it
def level02():

    st.write("# Data Viz Time!")
    st.write("We are creating sample data and displaying a linechart and map")

    # Create a linechart
    st.write("## Here's a Line Chart!")
    chart_data = pd.DataFrame(
        np.random.randn(20, 3),
        columns=['a', 'b', 'c'])

    st.line_chart(chart_data)

    # Plot a map
    st.write("## Here's a Map!")
    data = np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4]
    map_data = pd.DataFrame(data, columns=['lat', 'lon'])
    st.map(map_data)


# Call the first_app() function
level02()
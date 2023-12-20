import streamlit as st
import numpy as np
import pandas as pd

st.header("#My first Streamlit App")

option = st.sidebar.selectbox(
    'Select a mini project',
     ['line chart','map','T n C'])   #tajuk selectbox,[value]

if option=='line chart':
    chart_kau = pd.DataFrame(
      np.random.randn(20, 3),      #dia generate line chart dengan random value
      columns=['a', 'b', 'c'])
    st.line_chart(chart_kau)
elif option=='map':
    map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [3.1242, 101.6861],
    columns=['lat', 'lon'])
    st.map(map_data)
elif option=='T n C':
    st.write('Before you continue, please read the [terms and conditions](https://www.gnu.org/licenses/gpl-3.0.en.html)')
    show = st.checkbox('I agree the terms and conditions')
    if show:
        st.write(pd.DataFrame({
            'Students': ['John', 'Lofa', 'Siti', 'Amy'],
            'Attendance Status': ['yes', 'yes', 'yes', 'no']
        }))

import streamlit as st 
import pandas as pd
import numpy as np 

with st.sidebar: 
    st.image("https://www.onepointltd.com/wp-content/uploads/2020/03/inno2.png")
    st.title("Application Options")
    choice = st.radio("Navigation", ["Upload","Profiling","Modelling", "Download"])
    st.info("This project application helps you build and explore your data.")

st.title("EAM Data Validation")
st.text("This is going to do some cool shit, you wait and see")

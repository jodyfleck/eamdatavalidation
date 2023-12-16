import streamlit as st 
import pandas as pd
import numpy as np 

st.title("EAM Data Validation")
st.text("This is going to do some cool shit, you wait and see")

with st.sidebar: 
    st.image("https://www.onepointltd.com/wp-content/uploads/2020/03/inno2.png")
    st.title("Application Options")
    choice = st.radio("Navigation", ["Upload","Profiling","Modelling", "Download"])
    st.info("This project application helps you build and explore your data.")

if choice == "Upload":
    st.title("Upload Your Dataset")
    file = st.file_uploader("Upload Your Dataset")
    if file: 
        df = pd.read_csv(file, index_col=None)
        df.to_csv('dataset.csv', index=None)
        st.text("Upload successful, top 10 rows displayed")
        st.table(df.head(10))
        #st.dataframe(df)




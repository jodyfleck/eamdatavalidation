from operator import index
import streamlit as st 
import pandas as pd
import numpy as np 
#import plotly as px
#import matplotlib.pyplot as plt
#import seaborn
#import pandas_profiling
#from streamlit_pandas_profiling import st_profile_report 
#from pycaret.regression import setup, compare_models, pull, save_model, load_model

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
        # Display the count of rows and columns
        num_rows, num_cols = df.shape
        st.write(f"Success: Rows: {num_rows}, Columns: {num_cols}")
        st.table(df.head(10))
        #st.dataframe(df)

''''
        # Set the aesthetic style of the plots
        sns.set_style("whitegrid")

       --- # Plot this
        plt.figure(figsize=(8, 4))
        sns.barplot(x="Position", y="Salary", data=df)
        plt.title("Salary by Position")
        plt.xlabel("Position")
        plt.ylabel("Salary")
        plt.show()
'''



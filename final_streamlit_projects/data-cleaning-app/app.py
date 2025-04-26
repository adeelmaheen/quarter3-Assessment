# Imports
import streamlit as st
import pandas as pd
import os
from  io import BytesIO

# set up the app
st.set_page_config(page_title="💿 Data Sweeper", layout='wide')
st.title("💿 Data Sweeper")
st.write("Transform your files between CSV and Excel formats with built-in data cleaning app visualization!")

uploaded_files = st.file_uploader("Upload your files (CSV or Excel): ", type=["csv","xlsx"], accept_multiple_files=True)

if uploaded_files:
    for file in uploaded_files:
        file_ext = os.path.splitext(file.name)[-1].lower()


        if file_ext == ".csv":
            df = pd.read_csv(file)
        elif file_ext == ".xlsx":
            df = pd.read_excel(file)
        else:
            st.error(f"Unsupported file type: {file_ext}")
            continue

        # display input about file
        st.write(f"** File Name: ** {file.name}")
        st.write(f"** File Size: ** {file.size/1024}")

        # shows 5 rows of our df
        st.write("Preview the Head of our Dataframe")
        st.dataframe(df.head())

        # Options for data cleaning 
        st.subheader("Data Cleaning Options")
        if st.checkbox(f"Clean data for {file.name}"):
            col1,col2 = st.columns(2)


            with col1:
                if st.button(f"Remove Duplicate from {file.name}"):
                    df.drop_duplicates(inplace=True)
                    st.write("")
                


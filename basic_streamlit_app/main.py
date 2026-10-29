import streamlit as st
import pandas as pd

# Title and description
st.title("Video Game Sales")
st.write("With this app, you can explore how successful your favorite video games are!")

#Load the Kaggle dataset
df = pd.read_csv("basic_streamlit_app/data/vgsales.csv")

st.dataframe(df)
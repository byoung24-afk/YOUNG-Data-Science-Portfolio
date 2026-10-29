import streamlit as st
import pandas as pd

# Title and description
st.title("Video Game Sales")
st.write("With this app, you can explore how successful your favorite video games are!")

#Load the Kaggle dataset
df = pd.read_csv("basic_streamlit_app/data/vgsales.csv")

st.dataframe(df)

# --- Filters ---

# Dropdown selectbox with 'All' option + each unique genre, sorted A-Z
genre = st.sidebar.selectbox("Select a genre", ["All"] + sorted(df["Genre"].unique()))

# Second dropdown with 'All' option + each unique platform, sorted A-Z
platform = st.sidebar.selectbox("Select a platform", ["All"] + sorted(df["Platform"].unique()))

# Create a copy of the dataframe to apply filters without modifying the original
df_filtered = df.copy()


# Filter the dataframe based on the selected genre
if genre != "All":
    df_filtered = df[df["Genre"] == genre]
else:
    df_filtered = df

# Filter the dataframe based on the selected platform
if platform != "All":
    df_filtered = df_filtered[df_filtered["Platform"] == platform]

#Show the filtered dataframe
st.dataframe(df_filtered)
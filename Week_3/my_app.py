import streamlit as st

st.title("Hello, Streamlit!")
st.write("This is my first Streamlit app.")

if st.button(' Click me!'):
    st.write('Button clicked!')


color = st.color_picker('Pick a color', '#00f900')
st.write('The selected color is:', color)   

#  CSV File ssubheader
import pandas as pd
st.subheader("Exploring Our Dataset")

# Load the CSV file
df = pd.read_csv('data/sample_data.csv')

st.write("Here's our data:")
st.dataframe(df)

# Filter by city
city = st.selectbox('Select a city to filter by:', df['City'].unique())
filtered_df = df[df['City'] == city]

st.write(f"People in {city}:")
st.dataframe(filtered_df)

# Filter by occupation
occupation = st.selectbox('Select an occupation to filter by:', df['Occupation'].unique())
filtered_df_occupation = df[(df['City'] == city) & (df['Occupation'] == occupation)]

st.write(f"{occupation}s in {city}:")
st.dataframe(filtered_df_occupation)

st.subheader("Data Summaty")
st.write("Summary statistics of the dataset:")
st.write(df.describe()) 
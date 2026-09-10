import streamlit as st

st.title("Hello, Streamlit!")
st.write("This is my first Streamlit app.")

if st.button(' Click me!'):
    st.write('Button clicked!')
else st.write('Button not clicked yet.')

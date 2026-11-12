import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
st.title("Machine Learning Model Trainer")

#Radio button for user to select dataset
choice = st.radio("Choose your dataset:", ["Sample dataset (Penguins)", "Upload my own CSV"]) 

if choice == "Upload my own CSV":
    uploaded = st.file_uploader("Upload a CSV", type="csv")  # upload box
    if uploaded is None:
        st.stop()              # pause the app until a file arrives
    df = pd.read_csv(uploaded)
else:
    uploaded = "https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2020/2020-07-28/penguins.csv"  # use the sample dataset if user didn't upload one
    df = pd.read_csv(uploaded) # turn the file into a DataFrame
st.dataframe(df.head())  # show the first 5 rows of the dataset


df = df.dropna() # drop missing values

target = st.selectbox("Select the target variable:", df.columns) # Dropdown for user to select the target variable

y = df[target]  # target variable
X = df.drop(columns=target)  # features
X = pd.get_dummies(X)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
st.write(X_train.shape, X_test.shape)

max_depth = st.slider("Max depth", 1, 10, 3) # Slider for user to select max depth
min_samples_split = st.slider("Min samples split", 2, 20, 2) # Slider for user to select min samples split

model = DecisionTreeClassifier(max_depth=max_depth, min_samples_split=min_samples_split, random_state=42)  # create the model
model.fit(X_train, y_train) # train the model on the 80%
st.write("Model trained!")

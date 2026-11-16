import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from sklearn.metrics import ConfusionMatrixDisplay
import matplotlib.pyplot as plt

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

# Split the data into training and testing sets
y = df[target]  # target variable
# Stop if the target variable is not numeric
if pd.api.types.is_numeric_dtype(y) and y.nunique() > 20:
    st.warning("This model predicts categories. Pick a category column.")
    st.stop()

X = df.drop(columns=target)  # features
X = pd.get_dummies(X)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
st.write(X_train.shape, X_test.shape)

max_depth = st.slider("Max depth", 1, 10, 3) # Slider for user to select max depth
min_samples_split = st.slider("Min samples split", 2, 20, 2) # Slider for user to select min samples split

model = DecisionTreeClassifier(max_depth=max_depth, min_samples_split=min_samples_split, random_state=42)  # create the model
model.fit(X_train, y_train) # train the model on the 80%
st.write("Model trained!")



# Make predictions and calculate metrics
y_pred = model.predict(X_test)
st.write("Accuracy:", f"{accuracy_score(y_test, y_pred):.2%}")
st.write("Precision:", f"{precision_score(y_test, y_pred, average='weighted'):.2%}")
st.write("Recall:", f"{recall_score(y_test, y_pred, average='weighted'):.2%}")
st.write("F1 Score:", f"{f1_score(y_test, y_pred, average='weighted'):.2%}")


# Confusion Matrix
fig, ax = plt.subplots()                                       # blank chart
ConfusionMatrixDisplay.from_predictions(y_test, y_pred, ax=ax) # draw the matrix
st.subheader("Confusion Matrix")
st.pyplot(fig)                                                 # show it in the app
st.caption("Confusion Matrix: each row is the actual class, each column is the predicted class. " \
"The diagonal shows correct predictions. The off-diagonal shows misclassifications.")

# Explain the Metrics
st.subheader("Metrics Explanation")

st.write("Accuracy:" , f"{accuracy_score(y_test, y_pred):.2%}")
st.caption("Accuracy: the % of test rows the model predicted correctly.")

st.write("Precision:", f"{precision_score(y_test, y_pred, average='weighted'):.2%}")
st.caption("Precision: the % of positive predictions that were correct.")

st.write("Recall:", f"{recall_score(y_test, y_pred, average='weighted'):.2%}")
st.caption("Recall: the % of actual positives that were predicted correctly.")

st.write("F1 Score:", f"{f1_score(y_test, y_pred, average='weighted'):.2%}")
st.caption("F1 Score: One score that balances precision and recall.")
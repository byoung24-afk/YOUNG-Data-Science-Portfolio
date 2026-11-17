import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, DecisionTreeRegressor
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, r2_score, mean_absolute_error, root_mean_squared_error
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

df = df.dropna(axis=1, thresh=len(df) * 0.5) # drop columns with more than 50% missing values
df = df.dropna() # drop missing values

target = st.selectbox("Select the target variable:", df.columns) # Dropdown for user to select the target variable

# Split the data into training and testing sets
y = df[target]  # target variable
# decide which kind of model to train based on the target variable type
if pd.api.types.is_numeric_dtype(y) and y.nunique() > 20:
    task = "regression"
else:
    task = "classification"

st.write("Task type:", task) # Show the user which mode the app picked 

X_raw = df.drop(columns=target)  # features, kept for the input boxes
X = pd.get_dummies(X_raw)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
st.write(X_train.shape, X_test.shape)

max_depth = st.slider("Max depth", 1, 10, 3) # Slider for user to select max depth
min_samples_split = st.slider("Min samples split", 2, 20, 2) # Slider for user to select min samples split

if task == "classification":
    model = DecisionTreeClassifier(max_depth=max_depth, min_samples_split=min_samples_split, random_state=42)  # create the model
else:
    model = DecisionTreeRegressor(max_depth=max_depth, min_samples_split=min_samples_split, random_state=42)  # create the model
model.fit(X_train, y_train) # train the model on the 80%
st.write("Model trained!")



# Make predictions and calculate metrics
y_pred = model.predict(X_test)

if task == "classification":

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
    st.caption("Precision: When the model predicted a class, how often it's right.")

    st.write("Recall:", f"{recall_score(y_test, y_pred, average='weighted'):.2%}")
    st.caption("Recall: the % of actual positives that were predicted correctly.")

    st.write("F1 Score:", f"{f1_score(y_test, y_pred, average='weighted'):.2%}")
    st.caption("F1 Score: One score that balances precision and recall.")
else:
    # Regression Metrics
   
    # Residual Plot
    st.subheader("Residual Plot")
    residuals = y_test - y_pred                 # how far off each guess was
    fig, ax = plt.subplots()
    ax.scatter(y_pred, residuals)               # one dot per test row
    ax.axhline(0, color="red")                  # zero line = perfect guess
    ax.set_xlabel("Predicted value")
    ax.set_ylabel("Residual (actual − predicted)")
    st.pyplot(fig)
    st.caption("Residual plot: each dot is one test row. The red line means the model predicted perfectly. "
               "Dots scattered randomly around the line mean the model's errors are random; "
               "a pattern means the model is missing something.")

    # Explain the Metrics
    st.subheader("Metrics Explanation")

    st.write("Mean Absolute Error:", f"{mean_absolute_error(y_test, y_pred):.2f}")
    st.caption("Mean Absolute Error: on average, how far off the model's guesses are, in the target's units.")

    st.write("Root Mean Squared Error:", f"{root_mean_squared_error(y_test, y_pred):.2f}")
    st.caption("Root Mean Squared Error: like MAE, but big misses count extra.")

    st.write("R² Score:", f"{r2_score(y_test, y_pred):.2f}")
    st.caption("R² Score: how much of the target's ups and downs the model explains. 1 is perfect, 0 is no better than guessing the average.")

st.subheader("Make a Prediction")
user_input = {}                                    # holds the user's answers

for col in X_raw.columns:                          # one box per feature
    if pd.api.types.is_numeric_dtype(X_raw[col]):
        # number box, starting at the column's middle value
        user_input[col] = st.number_input(col, value=float(X_raw[col].median()))
    else:
        user_input[col] = st.selectbox(col, options=X_raw[col].unique())

if st.button("Predict"):
    row = pd.DataFrame([user_input])                          # one-row table from the answers
    row = pd.get_dummies(row)                                 # text to 0/1 columns
    row = row.reindex(columns=X.columns, fill_value=0)        # match the training columns
    prediction = model.predict(row)[0]                        # predict on the user's row
    st.success(f"Predicted {target}: {prediction:.2f}" if task == "regression" else f"Predicted {target}: {prediction}")
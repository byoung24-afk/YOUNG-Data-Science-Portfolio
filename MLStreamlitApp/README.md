# Machine Learning Model Trainer

## Overview
With this app, users can pick sample data or upload a CSV. Then the user chooses the target variable for the model to predict and sets the hyperparameters with the sliders. The app then displays metrics and a confusion matrix with the given inputs.

## Live App
[Open the app](https://young-data-science-portfolio-gtifiucokeftjs7ra5djlo.streamlit.app/)

## Run It Locally
1. Clone the repo: `git clone https://github.com/byoung24-afk/YOUNG-Data-Science-Portfolio`
2. Go into the folder: `cd YOUNG-Data-Science-Portfolio/MLStreamlitApp`
3. Install libraries: `pip install -r requirements.txt`
4. Run: `streamlit run app.py`

## Libraries
- streamlit==1.50.0
- pandas==2.3.3
- scikit-learn==1.6.1
- matplotlib==3.9.4

## Model & Hyperparameters
This model uses Decision Tree Classifier. The max_depth slider allows you to choose how deep the tree goes ranging from 1-10. The min_samples_split slider allows you to choose how many rows are required for the tree to split again; ranging from 2-20.

## Dataset
Palmer Penguins from TidyTuesday, plus the option to upload your own CSV

## References
- [Streamlit docs](https://docs.streamlit.io)
- [scikit-learn DecisionTreeClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.html)
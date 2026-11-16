# 📊 Bryce Young — Data Science Portfolio

## About This Portfolio
Code and projects for Introduction to Data Science. Includes machine learning projects and basic data cleaning projects

## Projects
- Project 1 - Building an interactive app
- Project 2 - Cleaning messy data
- How it fits - Together, these show both ends of a data science workflow: preparing data and presenting it.


## 🎮 Video Game Sales — Basic Streamlit App
Explore how successful your favorite video games are! Use the filters in the sidebar to narrow down the results.
- Folder: [`basic_streamlit_app/`](basic_streamlit_app/)
- Details and run instructions: see the [app README](basic_streamlit_app/README.md)


## 🏅 Tidy Data Project — 2008 Olympic Medalists
This project aims to clean up data from winners at the 2008 Olympics in order to better interpret what the data is telling us. This lets us understand which sports won the most medals, by how much, how men and women compare, etc. 
- Folder: [`TidyData-Project/`](TidyData-Project/)
- Details: see the [project README](TidyData-Project/README.md)

## Machine Learning Streamlit App
With this app, users can pick sample data or upload a CSV. Then the user chooses the target variable for the model to predict and sets the hyperparameters with the sliders. The app then displays metrics and a confusion matrix with the given inputs.

Building this app grew my understanding on ML. It helped me understanding how different prediction models are used for different circumstances. Also, my understanding on how to make models good at predicting data instead of memorizing their training set.

This app fits my portfolio because it combines interactive Python and prediction models to make an useful app.

- [App folder](https://github.com/byoung24-afk/YOUNG-Data-Science-Portfolio/tree/main/MLStreamlitApp)
- [Live app](https://young-data-science-portfolio-gtifiucokeftjs7ra5djlo.streamlit.app/)

**Other projects:** [Portfolio Update 1](https://github.com/byoung24-afk/YOUNG-Data-Science-Portfolio/tree/main/basic_streamlit_app) · [Portfolio Update 2](https://github.com/byoung24-afk/YOUNG-Data-Science-Portfolio/tree/main/TidyData-Project)
---
### Repository Structure 
```
Young-Data-Science-Portfolio/
├── README.md
├── basic_streamlit_app/
│   ├── README.md
│   ├── main.py
│   └── data/
│       └── vgsales.csv
└── TidyData-Project/
    ├── README.md
    ├── tidy_data_project.ipynb
    └── data/
        └── olympics_08_medalists.csv
```

Other folders ('Week_2', 'Week_3', 'Week_4', 'Week_7') hold weekly in-class exercises        


---

### How to Run the Streamlit App
```
pip install streamlit pandas
streamlit run basic_streamlit_app/main.py
```

---

## Coming Soon
More projects will be added throughout the semester



# 🎮 Video Game Sales

## About
With this app, you can explore how successful your favorite video games are! Use the filters in the sidebar to narrow down the results.

## Dataset
- **Source:** Video Game Sales dataset from Kaggle
- **What's in it:** One row represents a single game on one platform. Each game includes its name, release year, genre, publisher and sales in millions of copies for North America, Europe, Japan, other regions, and worldwide.

## Features
- Genre Dropdown Select Box — Filters all the games by the genre that you select.
- Platform Dropdown Select Box - Filters games by the console they were released on (e.g., Wii, PS2, Xbox 360)
- Year Select Slider - Let's you pick a range of release years to show only games from that time period.
- Interactive table of the filtered results

## How to Run
1. Install the required packages:
   ```
   pip install streamlit pandas
   ```
2. From the root of the repository, run:
   ```
   streamlit run basic_streamlit_app/main.py
   ```
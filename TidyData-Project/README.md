# 🏅 Tidy Data Project: 2008 Olympic Medalists

## Project Overview
This project aims to clean up data from winners at the 2008 Olympics in order to better interpret what the data is telling us. This lets us understand which sports won the most medals, by how much, how men and women compare, etc. 

### Tidy Data Principles
- Each Variable gets its own column.
- Each observation gets its own row.
- Each type of thing gets its own table.

## Dataset
- **Source:** 2008 Olympic Medalists (provided in class)
- **Raw format:** The raw data was hard to read and messy. Gender and sport were combined in the column headers. This breaks tidy rule #1: each variable should have its own column. There are a multitude of NaN cells that make the real data hard to see and also broke tidy rule #2: Each real observation gets its own row.
- **Cleaning steps:** melt → drop empty rows → split `event` into `gender` and `sport` → fix capitalization

## How to Run
1. Install dependencies:
   ```
   pip install pandas matplotlib seaborn
   ```
2. Open `tidy_data_project.ipynb` in VS Code or Jupyter
3. Run all cells top to bottom

## Key Findings
- In the 2008 Olympics, Athletics won the most gold medals. Most likely, because Athletics has a ton of events like sprints, distance, jumps, and throws.
- In the 2008 Olympics, males won more medals than females in each medal category. This could be because there were more male events than female events in the 2008 Olympics.

## References
- [Pandas Cheat Sheet](https://pandas.pydata.org/Pandas_Cheat_Sheet.pdf)
- [Tidy Data — Hadley Wickham](https://vita.had.co.nz/papers/tidy-data.pdf)
# 🎬 Movie Ratings Analysis

## IMDb Movie Dataset — Exploratory Data Analysis

An exploratory data analysis project examining relationships between movie ratings, runtime, genre, revenue, audience votes, and release year.

---

## 📌 Project Overview

This project analyzes a dataset of 1,000 movies released between 2006 and 2016.

The goal is to identify patterns and relationships in movie performance using Python and data visualization.

---

## 🎯 Objectives

- Analyze the relationship between movie runtime and IMDb rating
- Compare average IMDb ratings across genres
- Examine rating trends over time
- Investigate the relationship between revenue and IMDb rating
- Analyze the relationship between audience votes and IMDb rating
- Analyze the relationship between audience votes and revenue
- Identify the highest-rated movies in the dataset

---

## 📊 Dataset

The dataset contains 1,000 movie records and 12 variables.

### Important Variables

| Variable | Description |
|---|---|
| Title | Movie title |
| Genre | Movie genre(s) |
| Year | Release year |
| Runtime (Minutes) | Movie duration |
| Rating | IMDb rating |
| Votes | Number of audience votes |
| Revenue (Millions) | Reported movie revenue |
| Metascore | Critic score |

### Data Quality

- 1,000 movie records
- 12 variables
- 128 missing Revenue values
- 64 missing Metascore values
- 0 complete duplicate rows

Missing revenue values were not replaced with zero. Revenue-specific analysis was performed using records with reported revenue.

---

## 🔍 Analysis Performed

### 1. Runtime vs IMDb Rating

Correlation: **0.39**

Longer movies showed a moderate positive association with IMDb ratings in this dataset.

### 2. Genre vs IMDb Rating

War, Animation, and Biography had relatively high average ratings. Small sample sizes for some genres require cautious interpretation.

### 3. Ratings Over Time

Average IMDb ratings varied between 2006 and 2016, with relatively higher averages around 2006–2007 and lower averages toward 2015–2016.

### 4. Revenue vs IMDb Rating

Correlation: **0.22**

Revenue and IMDb rating showed a weak positive association.

### 5. Votes vs IMDb Rating

Correlation: **0.51**

Movies with more audience votes tended to have higher IMDb ratings in this dataset.

### 6. Votes vs Revenue

Correlation: **0.64**

Movies with more audience votes tended to have higher reported revenue.

### 7. Top 10 Highest-Rated Movies

The analysis identified the 10 highest-rated movies within the dataset.

---

## 📈 Visualizations

The project includes visualizations for:

- Runtime vs IMDb Rating
- Average Rating by Genre
- Average Rating by Year
- Revenue vs IMDb Rating
- Votes vs IMDb Rating
- Votes vs Revenue
- Top 10 Highest-Rated Movies

All charts are available in the `visualizations/` folder.

---

## 🛠️ Tools & Technologies

- Python
- Pandas
- Matplotlib
- Jupyter Notebook
- VS Code

---

## 📁 Project Structure

```text
Movie-Ratings-Analysis/
│
├── data/
│   └── IMDB-Movie-Data.csv
│
├── notebook/
│   └── movie_analysis.ipynb
│
├── visualizations/
│   ├── runtime_vs_rating.png
│   ├── genre_vs_rating.png
│   ├── rating_by_year.png
│   ├── revenue_vs_rating.png
│   ├── votes_vs_rating.png
│   ├── votes_vs_revenue.png
│   └── top_10_movies.png
│
├── README.md
└── requirements.txt
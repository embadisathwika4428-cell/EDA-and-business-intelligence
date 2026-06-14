 Exploratory Data Analysis (EDA) & Business Intelligence

OBJECTIVE
To uncover patterns, trends, and relationships within the Netflix Recommendations dataset and develop proficiency in SQL for data extraction and basic dashboarding.

DATASET OVERVIEW
Dataset   : Netflix Recommendations (Self-Generated)
Rows      : 155 titles
Columns   : 10 features
Format    : .xlsx

COLUMNS
Show_ID          - Unique identifier (NF0001 to NF0155)
Title            - Name of the show or movie
Genre            - Drama, Thriller, K-Drama, Sci-Fi, etc.
Content_Type     - Movie, TV Show, Mini-Series, Anime, etc.
Release_Year     - Year of release (2015 to 2024)
Age_Rating       - G, PG, PG-13, R, TV-MA, TV-14, etc.
IMDb_Score       - Rating from 5.5 to 9.5
Country_of_Origin- USA, South Korea, Spain, Germany, etc.
Language         - English, Korean, Spanish, etc.
Mood_Tag         - Binge-worthy, Dark, Romantic, Inspiring, etc.

TOOLS USED
- Python 3
- Pandas (Data Analysis)
- Matplotlib & Seaborn (Visualizations)
- SQLite (SQL Queries)
- Microsoft Excel (Dashboard)
- VS Code (IDE)

PROJECT STRUCTURE
Task-2-EDA/
├── data/
│   └── netflix_recommendations.xlsx
├── scripts/
│   ├── step1_eda_univariate.py
│   ├── step2_sql_business_questions.py
│   └── step3_multivariate_analysis.py
├── charts/
│   ├── step1_univariate_analysis.png
│   ├── step2_sql_results.png
│   ├── step3_heatmap.png
│   ├── step3_scatter.png
│   ├── step3_pairplot.png
│   ├── step3_boxplot.png
│   └── step3_genre_mood_heatmap.png
├── dashboard/
│   └── netflix_dashboard.xlsx
└── README.md

STEP 1 — DESCRIPTIVE STATISTICS & UNIVARIATE ANALYSIS
Script: scripts/step1_eda_univariate.py

- Dataset has 155 titles with no missing values
- IMDb scores range from 5.5 to 9.5 with a mean of around 7.5
- Content spans release years 2015 to 2024

Charts Generated:
1. IMDb Score Histogram with mean line
2. Content Type Bar Chart
3. Top 10 Genres
4. Release Year Distribution
5. Age Rating Pie Chart
6. Mood Tag Distribution

STEP 2 — SQL FOR BUSINESS QUESTIONS
Script: scripts/step2_sql_business_questions.py
Engine: Python built-in sqlite3 (no extra install needed)

Q1 - Top 10 highest rated titles         (ORDER BY, LIMIT)
Q2 - Average IMDb score by Genre          (GROUP BY, AVG)
Q3 - Number of titles released per year   (GROUP BY, COUNT)
Q4 - Top 5 content-producing countries    (GROUP BY, COUNT, LIMIT)
Q5 - Best rated content type              (GROUP BY, AVG)
Q6 - Mature titles (TV-MA) with IMDb > 8  (WHERE, filtering)
Q7 - Most common mood tag per genre       (Nested subquery, HAVING)

STEP 3 — MULTIVARIATE ANALYSIS & CORRELATION
Script: scripts/step3_multivariate_analysis.py

Charts Generated:
1. Correlation Heatmap — relationships between all features
2. Scatter Plot — IMDb Score vs Release Year by Genre
3. Strip Plot — IMDb Score across Content Types
4. Boxplot — IMDb Score distribution by Genre
5. Genre x Mood Tag Heatmap — which moods dominate each genre

Key Insights:
- K-Drama and Crime genres have consistently high IMDb scores
- Release year shows weak correlation with IMDb score
- TV-MA content dominates the high-rating tier (above 8.0)
- Binge-worthy and Suspenseful are the most common mood tags

STEP 4 — STATIC DASHBOARD MOCK-UP
File: dashboard/netflix_dashboard.xlsx

Sheet 1 - Dashboard   : KPI cards, 5 data tables, 3 embedded charts
Sheet 2 - Raw Data    : Full formatted 155-row dataset
Sheet 3 - KPI Summary : 10 key metrics with written insights

KPIs Tracked:
- Total Titles
- Average IMDb Score
- Highest Rated Title
- Top Genre and Top Country
- Content Type Share
- Age Rating Distribution
- Yearly Release Trend

HOW TO RUN
1. Install dependencies:
   pip install pandas matplotlib seaborn openpyxl

2. Run scripts:
   python scripts/step1_eda_univariate.py
   python scripts/step2_sql_business_questions.py
   python scripts/step3_multivariate_analysis.py

3. Open dashboard/netflix_dashboard.xlsx in Excel or Google Sheets


# ============================================================
#  TASK 2 - STEP 2: SQL for Business Questions
#  Using SQLite (built into Python - no install needed!)
# ============================================================

import pandas as pd
import sqlite3
import matplotlib.pyplot as plt
import seaborn as sns

# ── Load Excel into SQLite ────────────────────────────────────
df = pd.read_excel("netflix_recommendations.xlsx")
conn = sqlite3.connect(":memory:")
df.to_sql("netflix", conn, index=False, if_exists="replace")

print("✅ Dataset loaded into SQL table: 'netflix'")
print(f"   Rows: {len(df)} | Columns: {len(df.columns)}\n")

# ── Helper to run & display queries ──────────────────────────
def run_query(title, query):
    print("=" * 60)
    print(f"  {title}")
    print("=" * 60)
    result = pd.read_sql_query(query, conn)
    print(result.to_string(index=False))
    print()
    return result

# ────────────────────────────────────────────────────────────
# Q1: Top 10 highest rated titles on Netflix
# ────────────────────────────────────────────────────────────
q1 = run_query(
    "Q1: Top 10 Highest Rated Titles",
    """
    SELECT Title, Genre, Content_Type, IMDb_Score
    FROM netflix
    ORDER BY IMDb_Score DESC
    LIMIT 10
    """
)

# ────────────────────────────────────────────────────────────
# Q2: Average IMDb score by Genre
# ────────────────────────────────────────────────────────────
q2 = run_query(
    "Q2: Average IMDb Score by Genre",
    """
    SELECT Genre,
           COUNT(*) AS Total_Titles,
           ROUND(AVG(IMDb_Score), 2) AS Avg_IMDb,
           ROUND(MAX(IMDb_Score), 2) AS Max_IMDb
    FROM netflix
    GROUP BY Genre
    ORDER BY Avg_IMDb DESC
    """
)

# ────────────────────────────────────────────────────────────
# Q3: How many titles were released each year?
# ────────────────────────────────────────────────────────────
q3 = run_query(
    "Q3: Number of Titles Released Per Year",
    """
    SELECT Release_Year,
           COUNT(*) AS Total_Releases
    FROM netflix
    GROUP BY Release_Year
    ORDER BY Release_Year DESC
    """
)

# ────────────────────────────────────────────────────────────
# Q4: Top 5 countries producing the most content
# ────────────────────────────────────────────────────────────
q4 = run_query(
    "Q4: Top 5 Content-Producing Countries",
    """
    SELECT Country_of_Origin,
           COUNT(*) AS Total_Titles,
           ROUND(AVG(IMDb_Score), 2) AS Avg_Rating
    FROM netflix
    GROUP BY Country_of_Origin
    ORDER BY Total_Titles DESC
    LIMIT 5
    """
)

# ────────────────────────────────────────────────────────────
# Q5: Which Content_Type has the best average IMDb score?
# ────────────────────────────────────────────────────────────
q5 = run_query(
    "Q5: Best Rated Content Type",
    """
    SELECT Content_Type,
           COUNT(*) AS Count,
           ROUND(AVG(IMDb_Score), 2) AS Avg_IMDb
    FROM netflix
    GROUP BY Content_Type
    ORDER BY Avg_IMDb DESC
    """
)

# ────────────────────────────────────────────────────────────
# Q6: Titles rated TV-MA with IMDb score above 8.0
# ────────────────────────────────────────────────────────────
q6 = run_query(
    "Q6: Mature Titles (TV-MA) with IMDb > 8.0",
    """
    SELECT Title, Genre, IMDb_Score, Country_of_Origin
    FROM netflix
    WHERE Age_Rating = 'TV-MA' AND IMDb_Score > 8.0
    ORDER BY IMDb_Score DESC
    """
)

# ────────────────────────────────────────────────────────────
# Q7: Most common mood tag per genre
# ────────────────────────────────────────────────────────────
q7 = run_query(
    "Q7: Most Common Mood Tag per Genre",
    """
    SELECT Genre, Mood_Tag, COUNT(*) AS Count
    FROM netflix
    GROUP BY Genre, Mood_Tag
    HAVING COUNT(*) = (
        SELECT MAX(cnt) FROM (
            SELECT Genre AS g, COUNT(*) AS cnt
            FROM netflix n2
            WHERE n2.Genre = netflix.Genre
            GROUP BY Mood_Tag
        )
    )
    ORDER BY Genre
    """
)

# ── VISUALIZATIONS ────────────────────────────────────────────
sns.set_theme(style="darkgrid")
fig, axes = plt.subplots(2, 2, figsize=(16, 12))
fig.suptitle("Netflix - SQL Business Questions (Visual Results)", fontsize=16, fontweight="bold", color="#E50914")

# Q1 - Top 10 IMDb
axes[0, 0].barh(q1["Title"], q1["IMDb_Score"], color="#E50914")
axes[0, 0].set_title("Q1: Top 10 Highest Rated Titles")
axes[0, 0].set_xlabel("IMDb Score")
axes[0, 0].invert_yaxis()
axes[0, 0].set_xlim(0, 10)

# Q2 - Avg IMDb by Genre
axes[0, 1].bar(q2["Genre"], q2["Avg_IMDb"], color=sns.color_palette("Set2", len(q2)))
axes[0, 1].set_title("Q2: Avg IMDb Score by Genre")
axes[0, 1].set_ylabel("Avg IMDb")
axes[0, 1].tick_params(axis='x', rotation=45)

# Q3 - Releases per year
axes[1, 0].bar(q3["Release_Year"].astype(str), q3["Total_Releases"], color="#221F1F", edgecolor="#E50914")
axes[1, 0].set_title("Q3: Titles Released Per Year")
axes[1, 0].set_ylabel("Count")
axes[1, 0].tick_params(axis='x', rotation=30)

# Q4 - Top countries
axes[1, 1].bar(q4["Country_of_Origin"], q4["Total_Titles"], color=sns.color_palette("husl", 5))
axes[1, 1].set_title("Q4: Top 5 Content-Producing Countries")
axes[1, 1].set_ylabel("Total Titles")

plt.tight_layout()
plt.savefig("step2_sql_results.png", dpi=150, bbox_inches="tight")
plt.show()
print("✅ Chart saved as: step2_sql_results.png")

conn.close()
# ============================================================
#  TASK 2 - STEP 1: Descriptive Statistics & Univariate Analysis
#  Dataset: Netflix Recommendations
# ============================================================

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ── Load Dataset ─────────────────────────────────────────────
df = pd.read_excel("netflix_recommendations.xlsx")

print("=" * 55)
print("        NETFLIX DATASET - BASIC INFO")
print("=" * 55)
print(f"Shape        : {df.shape[0]} rows x {df.shape[1]} columns")
print(f"Columns      : {list(df.columns)}")
print(f"\nMissing Values:\n{df.isnull().sum()}")

# ── 1. DESCRIPTIVE STATISTICS ─────────────────────────────────
print("\n" + "=" * 55)
print("  DESCRIPTIVE STATISTICS (Numerical Columns)")
print("=" * 55)
print(df[["Release_Year", "IMDb_Score"]].describe().round(2))

print("\n" + "=" * 55)
print("  CATEGORICAL COLUMN SUMMARIES")
print("=" * 55)
for col in ["Genre", "Content_Type", "Age_Rating", "Country_of_Origin", "Mood_Tag", "Language"]:
    print(f"\n📌 {col} - Value Counts:")
    print(df[col].value_counts())

# ── 2. VISUALIZATIONS ─────────────────────────────────────────
sns.set_theme(style="darkgrid")
fig, axes = plt.subplots(3, 2, figsize=(16, 16))
fig.suptitle("Netflix Dataset - Univariate Analysis", fontsize=18, fontweight="bold", color="#E50914")

# --- Plot 1: IMDb Score Distribution (Histogram)
axes[0, 0].hist(df["IMDb_Score"], bins=15, color="#E50914", edgecolor="black")
axes[0, 0].set_title("IMDb Score Distribution")
axes[0, 0].set_xlabel("IMDb Score")
axes[0, 0].set_ylabel("Count")
axes[0, 0].axvline(df["IMDb_Score"].mean(), color="gold", linestyle="--", label=f"Mean: {df['IMDb_Score'].mean():.2f}")
axes[0, 0].legend()

# --- Plot 2: Content Type Bar Chart
ct_counts = df["Content_Type"].value_counts()
axes[0, 1].bar(ct_counts.index, ct_counts.values, color=sns.color_palette("Set2", len(ct_counts)))
axes[0, 1].set_title("Content Type Distribution")
axes[0, 1].set_xlabel("Content Type")
axes[0, 1].set_ylabel("Count")
axes[0, 1].tick_params(axis='x', rotation=20)

# --- Plot 3: Genre Bar Chart (Top 10)
genre_counts = df["Genre"].value_counts().head(10)
axes[1, 0].barh(genre_counts.index, genre_counts.values, color="#E50914")
axes[1, 0].set_title("Top 10 Genres")
axes[1, 0].set_xlabel("Count")
axes[1, 0].invert_yaxis()

# --- Plot 4: Release Year Distribution
year_counts = df["Release_Year"].value_counts().sort_index()
axes[1, 1].bar(year_counts.index, year_counts.values, color="#221F1F", edgecolor="#E50914")
axes[1, 1].set_title("Content by Release Year")
axes[1, 1].set_xlabel("Year")
axes[1, 1].set_ylabel("Count")

# --- Plot 5: Age Rating Pie Chart
rating_counts = df["Age_Rating"].value_counts()
axes[2, 0].pie(rating_counts.values, labels=rating_counts.index, autopct="%1.1f%%",
               colors=sns.color_palette("Set3", len(rating_counts)), startangle=140)
axes[2, 0].set_title("Age Rating Breakdown")

# --- Plot 6: Mood Tag Bar Chart
mood_counts = df["Mood_Tag"].value_counts()
axes[2, 1].bar(mood_counts.index, mood_counts.values, color=sns.color_palette("husl", len(mood_counts)))
axes[2, 1].set_title("Mood Tag Distribution")
axes[2, 1].set_xlabel("Mood")
axes[2, 1].set_ylabel("Count")
axes[2, 1].tick_params(axis='x', rotation=30)

plt.tight_layout()
plt.savefig("step1_univariate_analysis.png", dpi=150, bbox_inches="tight")
plt.show()
print("\n✅ Chart saved as: step1_univariate_analysis.png")
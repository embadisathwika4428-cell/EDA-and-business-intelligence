# ============================================================
#  TASK 2 - STEP 3: Multivariate Analysis & Correlation
#  Scatter plots, Heatmaps, Pair plots
# ============================================================

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.gridspec import GridSpec

# ── Load Dataset ─────────────────────────────────────────────
df = pd.read_excel("netflix_recommendations.xlsx")

# Encode categorical columns as numbers for correlation
df_encoded = df.copy()
df_encoded["Genre_Code"]        = df["Genre"].astype("category").cat.codes
df_encoded["ContentType_Code"]  = df["Content_Type"].astype("category").cat.codes
df_encoded["Rating_Code"]       = df["Age_Rating"].astype("category").cat.codes
df_encoded["Country_Code"]      = df["Country_of_Origin"].astype("category").cat.codes
df_encoded["Mood_Code"]         = df["Mood_Tag"].astype("category").cat.codes

sns.set_theme(style="darkgrid")

# ══════════════════════════════════════════════════════════════
#  FIGURE 1 — Correlation Heatmap
# ══════════════════════════════════════════════════════════════
fig1, ax1 = plt.subplots(figsize=(10, 7))

corr_cols = ["IMDb_Score", "Release_Year", "Genre_Code",
             "ContentType_Code", "Rating_Code", "Country_Code", "Mood_Code"]
corr_matrix = df_encoded[corr_cols].corr()

sns.heatmap(
    corr_matrix, annot=True, fmt=".2f", cmap="RdYlGn",
    linewidths=0.5, ax=ax1, vmin=-1, vmax=1,
    xticklabels=["IMDb", "Year", "Genre", "Type", "Rating", "Country", "Mood"],
    yticklabels=["IMDb", "Year", "Genre", "Type", "Rating", "Country", "Mood"]
)
ax1.set_title("Correlation Heatmap — Netflix Features", fontsize=15, fontweight="bold", color="#E50914")
plt.tight_layout()
plt.savefig("step3_heatmap.png", dpi=150, bbox_inches="tight")
plt.show()
print("✅ Saved: step3_heatmap.png")

# ══════════════════════════════════════════════════════════════
#  FIGURE 2 — Scatter Plots (2 relationships)
# ══════════════════════════════════════════════════════════════
fig2, axes = plt.subplots(1, 2, figsize=(16, 6))
fig2.suptitle("Scatter Plot Analysis", fontsize=15, fontweight="bold", color="#E50914")

# Scatter 1: IMDb Score vs Release Year (colored by Genre)
genre_list = df["Genre"].unique()
palette = sns.color_palette("tab20", len(genre_list))
genre_color = {g: palette[i] for i, g in enumerate(genre_list)}

for genre in genre_list:
    subset = df[df["Genre"] == genre]
    axes[0].scatter(subset["Release_Year"], subset["IMDb_Score"],
                    label=genre, color=genre_color[genre], alpha=0.75, s=60)

axes[0].set_title("IMDb Score vs Release Year (by Genre)")
axes[0].set_xlabel("Release Year")
axes[0].set_ylabel("IMDb Score")
axes[0].legend(fontsize=6, loc="lower left", ncol=2)

# Scatter 2: IMDb Score vs Content Type (strip plot)
sns.stripplot(
    data=df, x="Content_Type", y="IMDb_Score",
    palette="Set2", jitter=True, size=7, ax=axes[1]
)
axes[1].set_title("IMDb Score Distribution by Content Type")
axes[1].set_xlabel("Content Type")
axes[1].set_ylabel("IMDb Score")
axes[1].tick_params(axis='x', rotation=20)

plt.tight_layout()
plt.savefig("step3_scatter.png", dpi=150, bbox_inches="tight")
plt.show()
print("✅ Saved: step3_scatter.png")

# ══════════════════════════════════════════════════════════════
#  FIGURE 3 — Pair Plot (key numeric + encoded columns)
# ══════════════════════════════════════════════════════════════
pair_df = df_encoded[["IMDb_Score", "Release_Year", "Genre_Code", "Rating_Code"]].copy()
pair_df.columns = ["IMDb Score", "Release Year", "Genre", "Age Rating"]

pair_plot = sns.pairplot(
    pair_df,
    diag_kind="kde",
    plot_kws={"alpha": 0.5, "color": "#E50914"},
    diag_kws={"color": "#221F1F"}
)
pair_plot.fig.suptitle("Pair Plot — Netflix Key Variables", y=1.02,
                        fontsize=14, fontweight="bold", color="#E50914")
plt.savefig("step3_pairplot.png", dpi=150, bbox_inches="tight")
plt.show()
print("✅ Saved: step3_pairplot.png")

# ══════════════════════════════════════════════════════════════
#  FIGURE 4 — Boxplot: IMDb Score by Genre
# ══════════════════════════════════════════════════════════════
fig4, ax4 = plt.subplots(figsize=(14, 6))
genre_order = df.groupby("Genre")["IMDb_Score"].median().sort_values(ascending=False).index

sns.boxplot(data=df, x="Genre", y="IMDb_Score", order=genre_order,
            palette="Set3", ax=ax4)
ax4.set_title("IMDb Score Distribution by Genre (Boxplot)", fontsize=14,
              fontweight="bold", color="#E50914")
ax4.set_xlabel("Genre")
ax4.set_ylabel("IMDb Score")
ax4.tick_params(axis='x', rotation=35)

plt.tight_layout()
plt.savefig("step3_boxplot.png", dpi=150, bbox_inches="tight")
plt.show()
print("✅ Saved: step3_boxplot.png")

# ══════════════════════════════════════════════════════════════
#  FIGURE 5 — Heatmap: Genre vs Mood Tag (count)
# ══════════════════════════════════════════════════════════════
fig5, ax5 = plt.subplots(figsize=(14, 7))
pivot = df.pivot_table(index="Genre", columns="Mood_Tag", aggfunc="size", fill_value=0)

sns.heatmap(pivot, annot=True, fmt="d", cmap="YlOrRd",
            linewidths=0.4, ax=ax5)
ax5.set_title("Genre vs Mood Tag — Content Count Heatmap",
              fontsize=14, fontweight="bold", color="#E50914")
ax5.set_xlabel("Mood Tag")
ax5.set_ylabel("Genre")
ax5.tick_params(axis='x', rotation=35)

plt.tight_layout()
plt.savefig("step3_genre_mood_heatmap.png", dpi=150, bbox_inches="tight")
plt.show()
print("✅ Saved: step3_genre_mood_heatmap.png")

print("\n✅ Step 3 Complete! All 5 charts saved.")
print("   → step3_heatmap.png")
print("   → step3_scatter.png")
print("   → step3_pairplot.png")
print("   → step3_boxplot.png")
print("   → step3_genre_mood_heatmap.png")
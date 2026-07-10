import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats




df = pd.read_csv("cinema_dataset.csv")


# Genre Mapping

genre_map = {
    0: "Action",
    1: "Comedy",
    2: "Drama",
    3: "Horror",
    4: "Sci-Fi",
    5: "Romance"
}
df["movie_genre"] = df["movie_genre"].map(genre_map)


# Handle Missing Data

missing_percent = df.isna().mean() * 100

# Drop rows with NaN in columns where missing < 1%

drop_cols = missing_percent[missing_percent < 1].index
df_clean = df.dropna(subset=drop_cols)

# Fill remaining NaN values

fill_cols = missing_percent[missing_percent >= 1].index

for col in fill_cols:
    if col in ["ticket_price", "snacks_spent"]:
        df_clean[col] = df_clean.groupby("movie_genre")[col].transform(lambda x: x.fillna(np.mean(x)))
    elif col == "rating":
        df_clean[col] = df_clean[col].fillna(np.mean(df_clean[col]))
    elif np.issubdtype(df_clean[col].dtype, np.number):
        
        df_clean[col] = df_clean[col].fillna(np.mean(df_clean[col]))
    else:
        
        df_clean[col] = df_clean[col].fillna(df_clean[col].mode()[0])



# ---------------------



numerical_cols = df_clean.select_dtypes(include=np.number).columns
summary_data = []

for col in numerical_cols:
    col_data = df_clean[col].dropna()
    summary_data.append({
        "Column": col,
        "Mean": np.mean(col_data),
        "Median": np.median(col_data),
        "Mode": df_clean[col].mode()[0],
        "Variance": np.var(col_data),
        "Std Deviation": np.std(col_data),
        "Min": np.min(col_data),
        "Max": np.max(col_data),
        "25%": np.percentile(col_data, 25),
        "75%": np.percentile(col_data, 75)
    })

summary_df = pd.DataFrame(summary_data)
summary_df.to_csv("Descriptive_Statistics.csv", index=False)


# ---------------------


# Rating by Genre

plt.figure(figsize=(7, 4))
df_clean.groupby("movie_genre")["rating"].mean().plot(kind="bar", color="skyblue")
plt.title("Average Rating by Genre")
plt.ylabel("Rating")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("plot_rating_by_genre.png")
plt.close()

# Snacks Spent by Genre

plt.figure(figsize=(7, 4))
df_clean.groupby("movie_genre")["snacks_spent"].mean().plot(kind="bar", color="orange")
plt.title("Average Snacks Spent by Genre")
plt.ylabel("Snacks Spent")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("plot_snacks_by_genre.png")
plt.close()

# Ticket Price Weekday vs Weekend

plt.figure(figsize=(6, 4))
df_clean.groupby("weekend")["ticket_price"].mean().plot(kind="bar", color=["gray", "green"])
plt.title("Ticket Price: Weekday vs Weekend")
plt.xticks([0, 1], ["Weekday", "Weekend"], rotation=0)
plt.ylabel("Avg Ticket Price")
plt.tight_layout()
plt.savefig("plot_ticket_weekday_vs_weekend.png")
plt.close()

# Age Distribution

plt.figure(figsize=(8, 5))
plt.hist(df_clean["age"], bins=20, color="lightgreen", edgecolor="black")
plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.tight_layout()
plt.savefig("plot_age_distribution.png")
plt.close()

# Loyalty Score vs Rating 

plt.figure(figsize=(7, 5))
plt.scatter(df_clean["loyalty_score"], df_clean["rating"], alpha=0.5, color="purple")
plt.title("Loyalty Score vs Rating")
plt.xlabel("Loyalty Score")
plt.ylabel("Rating")
plt.tight_layout()
plt.savefig("plot_loyalty_vs_rating.png")
plt.close()

#Ticket Price vs Snacks Spent 

plt.figure(figsize=(7, 5))
plt.scatter(df_clean["ticket_price"], df_clean["snacks_spent"], alpha=0.5, color="red")
plt.title("Ticket Price vs Snacks Spent")
plt.xlabel("Ticket Price")
plt.ylabel("Snacks Spent")
plt.tight_layout()
plt.savefig("plot_ticket_vs_snacks.png")
plt.close()

# Age vs Rating

plt.figure(figsize=(7, 5))
plt.scatter(df_clean["age"], df_clean["rating"], alpha=0.5, color="teal")
plt.title("Age vs Rating")
plt.xlabel("Age")
plt.ylabel("Rating")
plt.tight_layout()
plt.savefig("plot_age_vs_rating.png")
plt.close()

# ---------------------

print("analysis done !")
print("csv and pngs have been saved !")

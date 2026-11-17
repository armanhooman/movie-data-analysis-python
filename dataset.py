import pandas as pd
import numpy as np

np.random.seed(42)

n_rows = 10000

# Generate synthetic features with correlations
age = np.random.normal(30, 10, n_rows).clip(10, 70)
gender = np.random.choice([0, 1], size=n_rows)
movie_genre = np.random.choice([0, 1, 2, 3, 4], size=n_rows)
visit_time = np.random.randint(10, 24, size=n_rows)
weekend = np.random.choice([0, 1], size=n_rows, p=[0.7, 0.3])
group_size = np.random.poisson(2, size=n_rows).clip(1, 10)

ticket_price = 10 + movie_genre * 1.5 + weekend * 2 + np.random.normal(0, 1.5, n_rows)
snacks_spent = group_size * np.random.normal(5, 1.5, n_rows)
rating = 6 + (1 - abs(movie_genre - 2) / 2) + np.random.normal(0, 1, n_rows)
loyalty_score = (10 - np.abs(age - 30)/6) + rating/2 + np.random.normal(0, 1, n_rows)

# Assemble into DataFrame
df = pd.DataFrame({
    'age': age,
    'gender': gender,
    'movie_genre': movie_genre,
    'ticket_price': ticket_price,
    'snacks_spent': snacks_spent,
    'rating': rating.clip(1, 10),
    'visit_time': visit_time,
    'weekend': weekend,
    'group_size': group_size,
    'loyalty_score': loyalty_score
})

# Specify different missing rates for each column
missing_rates = {
    'age': 0.10,
    'gender': 0.15,
    'movie_genre': 0.05,
    'ticket_price': 0.25,
    'snacks_spent': 0.30,
    'rating': 0.20,
    'visit_time': 0.12,
    'weekend': 0.18,
    'group_size': 0.08,
    'loyalty_score': 0.22
}

# Apply NaNs based on the defined rates
for col, rate in missing_rates.items():
    df.loc[df.sample(frac=rate).index, col] = np.nan

# View sample output and null percentages
print(df.head())
print("\nPercentage of NaNs per column:\n", df.isnull().mean().round(2))

try:
    df.to_csv('cinema_dataset.csv', index=False)
    print("cinema data set added to csv")
except Exception as e:
    print(f"error :  {e}")
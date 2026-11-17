# 🎬 Movie Data Analysis with Python

A Python exploratory data analysis project built around a **synthetic cinema dataset with 10,000 records**. The project covers dataset generation, missing-value handling, descriptive statistics, grouped analysis, and data visualization.

> **Dataset note:** The data is synthetic and was created for educational purposes. It does not represent real customers, cinemas, or movie performance.

## Project Goals

- Generate a structured synthetic dataset for analysis
- Introduce controlled missing values
- Clean and preprocess the dataset
- Calculate descriptive statistics
- Compare groups such as genres and weekday/weekend visits
- Explore relationships between numerical variables
- Produce reusable CSV and PNG analysis outputs

## Technologies

- Python
- Pandas
- NumPy
- Matplotlib
- SciPy

## Dataset

The dataset contains 10,000 cinema-visit records with features such as:

- Age
- Gender
- Movie genre
- Ticket price
- Snacks spending
- Rating
- Visit time
- Weekend indicator
- Group size
- Loyalty score

The generator intentionally introduces different missing-value rates across columns so that data-cleaning techniques can be practiced.

## Data Cleaning

The analysis script:

- Calculates missing-value percentages
- Drops rows for columns with very low missingness
- Fills remaining numerical missing values using means
- Uses genre-based mean imputation for selected financial columns
- Uses the mode for categorical values
- Maps numerical genre codes to readable genre names

## Descriptive Statistics

For numerical columns, the project calculates:

- Mean
- Median
- Mode
- Variance
- Standard deviation
- Minimum
- Maximum
- 25th percentile
- 75th percentile

The results are saved to:

```text
Descriptive_Statistics.csv
```

## Visualizations

The project generates multiple plots, including:

- Average rating by genre
- Average snacks spending by genre
- Average ticket price on weekdays vs weekends
- Age distribution
- Loyalty score vs rating
- Ticket price vs snacks spending
- Age vs rating

The generated charts are saved as PNG files.

## Project Structure

```text
movie-data-analysis-python/
├── main.py
├── dataset.py
├── cinema_dataset.csv
├── Descriptive_Statistics.csv
├── requirements.txt
├── data analysis Report.pdf
├── plot_age_distribution.png
├── plot_age_vs_rating.png
├── plot_loyalty_vs_rating.png
├── plot_rating_by_genre.png
├── plot_snacks_by_genre.png
├── plot_ticket_vs_snacks.png
├── plot_ticket_weekday_vs_weekend.png
└── README.md
```

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/armanhooman/movie-data-analysis-python.git
cd movie-data-analysis-python
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Optional: regenerate the synthetic dataset

```bash
python dataset.py
```

### 4. Run the analysis

```bash
python main.py
```

Running the analysis recreates the descriptive-statistics CSV and visualization files.

## Learning Outcomes

Through this project I practiced:

- Synthetic dataset generation
- Missing-data analysis and imputation
- Pandas DataFrame operations
- GroupBy analysis
- Descriptive statistics
- NumPy numerical functions
- Data visualization with Matplotlib
- Exporting analytical results to files

## Report

A PDF report describing the analysis is included in the repository as:

```text
data analysis Report.pdf
```

## Author

**Arman Hooman**

Computer Science student focused on Python, SQL, Data Analysis, and AI Engineering.

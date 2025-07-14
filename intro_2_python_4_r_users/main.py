####https://occasionaldivergences.com/posts/python-intro/####

# 1. Get started

# Install python and initialize the project environment with uv
# Install with "uv pip install"

# A) Data wrangling

# Import data

import polars as pl
import os

# With os - check working directory with os.getcwd() and os.listdir('.')

customer_data = pl.read_csv(os.path.join('python_tutorials', 'intro_2_python_4_r_users', 'data', 'customer_data.csv'))
customer_data.shape

customer_data.columns

# Filter observations

customer_data.filter(pl.col('gender') == 'Female', pl.col('income') > 70000)

# Slice observations

customer_data.slice(0, 5)

# Sort observations

customer_data.sort(pl.col('birth_year'), descending = True)

# Select variables

customer_data.select(pl.col(['region', 'review_text']))

# Create new variables

customer_data.with_columns(income = pl.col('income') / 1000)

# Join data frames

store_transactions = pl.read_csv(os.path.join('python_tutorials', 'intro_2_python_4_r_users', 'data', 'store_transactions.csv'))
customer_data.join(store_transactions, on='customer_id', how='left')

# Consecutive lines of code

(customer_data
  .join(store_transactions, on='customer_id', how='left')
  .filter(pl.col('region') == 'West', pl.col('feb_2005') == pl.col('feb_2005').max())
  .with_columns(age = 2024 - pl.col('birth_year'))
  .select(pl.col(['age', 'feb_2005']))
  .sort(pl.col('age'), descending=True)
  .slice(0, 1)
)

# Summarize discrete data

(customer_data
  .group_by(pl.col(['region', 'college_degree']))
  .agg(n = pl.len())
)

# Summarize continuous data

(customer_data
  .select(pl.col(['income', 'credit']))
  .mean()
)

# Summarize discrete and continuous data

(customer_data
  .group_by(pl.col(['gender', 'region']))
  .agg(
    n = pl.len(), 
    avg_income = pl.col('income').mean(), 
    avg_credit = pl.col('credit').mean()
  )
  .sort(pl.col('avg_income'), descending=True)
)

# Lazy evaluation

df = (customer_data
  .group_by(pl.col(['gender', 'region']))
  .agg(
    n = pl.len(), 
    avg_income = pl.col('income').mean(), 
    avg_credit = pl.col('credit').mean()
  )
  .sort(pl.col('avg_income'), descending=True)
).lazy()

df.explain()

df.collect()

# B) Visualization

# Column plots

import seaborn.objects as so

region_count = (customer_data
  .group_by(pl.col('region'))
  .agg(n = pl.len())
)

(so.Plot(region_count, x = 'region', y = 'n')
  .add(so.Bar())
)

(so.Plot(customer_data, x = 'region')
  .add(so.Bar(), so.Hist())
)

region_count = (customer_data
  .group_by(pl.col(['region', 'college_degree']))
  .agg(n = pl.len())
)

(so.Plot(region_count, x = 'region', y = 'n', color = 'college_degree')
  .add(so.Bar(), so.Agg(), so.Dodge())
)

region_count = (customer_data
  .group_by(pl.col(['region', 'college_degree']))
  .agg(n = pl.len())
)

(so.Plot(region_count, x = 'region', y = 'n', color = 'college_degree')
  .add(so.Bar(), so.Agg(), so.Dodge())
)

# Histograms

(so.Plot(customer_data, x = 'income', color = 'region')
  .add(so.Bars(), so.Hist())
)

# Scatterplots

(so.Plot(customer_data, x = 'income', y = 'credit')
  .add(so.Dot())
)

(so.Plot(customer_data, x = 'star_rating', y = 'income')
  .add(so.Dot(pointsize = 10, alpha = 0.5), so.Jitter(0.75))
)

# Line plots

(so.Plot(customer_data, x = 'review_time', y = 'star_rating')
  .add(so.Line())
)

rating_data = (customer_data
  .drop_nulls(pl.col('star_rating'))
  .select(pl.col(['review_time', 'star_rating']))
  .with_columns(
    pl.col('review_time').str.to_date(format='%m %d, %Y').alias('review_time')
  )
  .with_columns(
    pl.col('review_time').dt.year().alias('review_year')
  )
  .group_by('review_year')
  .agg(pl.mean('star_rating').alias('avg_star_rating'))
)

(so.Plot(rating_data, x = 'review_year', y = 'avg_star_rating')
  .add(so.Line())
)

# Density plots

(so.Plot(customer_data, x = 'income', color = 'gender')
  .add(so.Area(), so.Hist())
)

# Facets

region_count = (customer_data
  .group_by(pl.col(['region', 'college_degree', 'gender']))
  .agg(n = pl.len())
)

(so.Plot(region_count, x = 'region', y = 'n', color = 'college_degree')
  .facet('gender')
  .add(so.Bar(), so.Agg(), so.Dodge())
)

# C) Modeling

# Prepare data

# sklearn is very big - import individual libraries...

import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.metrics import root_mean_squared_error

# Set seed, variable, and parameter values.
np.random.seed(42)
nobs = 500
beta0 = -5
beta1 = 5
beta2 = 2
beta3 = 0

# Simulate data.
sim_data = pl.DataFrame({
    'x1': np.round(np.random.uniform(0, 20, nobs)),
    'x2': np.random.choice(['level01', 'level02', 'level03'], nobs, p = [0.7, 0.2, 0.1]),
    'y': beta0 + beta1 * np.random.uniform(0, 20, nobs) + beta2 * (np.random.choice(['level01', 'level02', 'level03'], nobs, p=[0.7, 0.2, 0.1]) == 'level02') + beta3 * (np.random.choice(['level01', 'level02', 'level03'], nobs, p=[0.7, 0.2, 0.1]) == 'level03') + np.random.normal(0, 3, nobs)
})

sim_data

# Training and testing split.
X = sim_data.drop('y').to_pandas()
y = sim_data['y'].to_pandas()
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=42)

# Feature engineering.
categorical_features = ['x2']
categorical_transformer = Pipeline(steps=[
  ('onehot', OneHotEncoder(handle_unknown='ignore'))
])

preprocessor = ColumnTransformer(
  transformers=[
      ('cat', categorical_transformer, categorical_features)
  ]
)

# Specify and fit a model

# Model specification.
model = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('regressor', LinearRegression())
])

# Fit the model.
model.fit(X_train, y_train)

# Evaluate model fit

# Compute RMSE.
y_pred = model.predict(X_test)
root_mean_squared_error(y_test, y_pred)

# D) Communication


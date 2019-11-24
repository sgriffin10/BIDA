import pandas as pd
import numpy as np
flights = pd.read_csv("http://rcs.bu.edu/examples/python/data_analysis/flights.csv")

desired_width=320
pd.set_option('display.width', desired_width)
np.set_printoptions(linewidth=desired_width)
pd.set_option('display.max_columns',12)

print(flights.head())
# Select the rows that have at least one missing value
# print(flights[flights.isnull().any(axis=1)].head())
# # Filter all the rows where arr_delay value is missing:
# flights1 = flights[ flights['arr_delay'].notnull( )]
# print(flights1.head())1
# # Remove all the observations with missing values
# flights2 = flights.dropna()
# # Fill missing values with zeros
# nomiss =flights['dep_delay'].fillna(0)
# nomiss.isnull().any()
# # Count how many missing data are in dep_delay and arr_delay columns
# print(flights[['dep_delay','arr_delay']].isnull().sum())
# # Let's compute summary statistic per a group':
# print(flights.groupby('carrier')['dep_delay'].mean())
# # Convinient describe() function computes a veriety of statistics
# print(flights.dep_delay.describe())
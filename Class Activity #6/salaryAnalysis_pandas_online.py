import pandas as pd

#Read csv file - from the Internet!
df = pd.read_csv("http://rcs.bu.edu/examples/python/data_analysis/Salaries.csv")
#Check the type of a column "salary"
print(df['salary'].dtype)
#Check the datatypes of all other columns
print(df.dtypes)
#Check the structure of the dataframe (number of rows and columns)
print(df.shape)
print(df.describe)

#Printing optins - just specfic to the PyCharm output
import numpy as np # imports can be anywhere before use!
desired_width=320
pd.set_option('display.width', desired_width)
np.set_printoptions(linewidth=desired_width)
pd.set_option('display.max_columns',12)

# Grouping data
print(df.groupby('rank').describe())
print(df.groupby('rank')['salary'].describe())
print(df.sort_values(by = 'rank'))
# Visualization - generate a histogram for each of the Series in the dataset
import matplotlib.pyplot as plt
df.hist()
plt.show()

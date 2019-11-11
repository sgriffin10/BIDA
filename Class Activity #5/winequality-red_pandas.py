# # Import the necessary modules
#
# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt
#
# # Create a dataframe from one line of code
# df = pd.read_csv("C:\\<fullPathTo>\winequality-red.csv", sep = ';')
#
# # Get statistics
# print(df.describe())
# # Get datatypes within the Series.  Note that Pandas automatically detected numerical values
# print(df.dtypes)
# # Get the statistics from just one column
# print(df['quality"""'].describe())
#
# # Visualization - generate a histogram for each of the Series in the dataset
# df.hist()
# plt.show()
#
# # Printing output - making sure that we can see all the columns
# # Specific only to PyCharm
# desired_width=320
#
# pd.set_option('display.width', desired_width)
#
# np.set_printoptions(linewidth=desired_width)
#
# pd.set_option('display.max_columns',12)
#
# # Now we can see all the values
# print(df.describe())
# print(df.dtypes)
# print(df['quality"""'].describe())
#
# # Pivot / Transpose - make columns into rows and vice-versa
# print(df.T)
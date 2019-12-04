from sklearn.datasets import load_boston
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import metrics
import numpy as np
from sklearn.datasets.california_housing import fetch_california_housing

cali = fetch_california_housing();
print(cali.DESCR)
print(cali.data.shape)
print(type(cali))
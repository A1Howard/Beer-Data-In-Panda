
import pandas as pd
import numpy as np

filename = 'Inventories/2018-02-28_12:35:40.880574.csv'
inventory = pd.read_csv(filename)

inventory = inventory.iloc[:, 0:7]
# print(inventory.head())
# print(inventory.corr())

print(inventory.describe())

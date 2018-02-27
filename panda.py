
import pandas as pd
import numpy as np

filename = 'Inventories/2018-02-26_16:18:25.458346.csv'
inventory = pd.read_csv(filename)

inventory = inventory.iloc[:, 0:7]
# print(inventory.head())
# print(inventory.corr())

print(inventory.describe())

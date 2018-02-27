
import pandas as pd

filename = '2018-02-26_16:18:25.458346.csv'
inventory = pd.read_csv(filename)

inventory = inventory.iloc[:, 0:7]
# print(inventory.head())
# print(inventory.corr())

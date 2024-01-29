# ASSOCIATION RULE

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import association_rules, apriori

dataset1 = pd.read_csv("Market Basket Analysis - Groceries_dataset.csv")
dataset2 = pd.read_csv("movies_genre.csv")

dataset = pd.read_csv("Market_Basket_Optimisation.csv", header = None)

# ---> Data Cleaning and Transformation Phase
# TASK 1: Create a list of lists
Transactions = []

for row in range(0, 7501):
    each_transaction = []
    for column in range(0, 20):
        item = dataset.iloc[row, column]
        if not isinstance(item, float):
            each_transaction.append(item)
    Transactions.append(each_transaction)

# TASK 2: Create an ENCODED VERSION of your data
encoder = TransactionEncoder()
new_data = pd.DataFrame(encoder.fit_transform(Transactions), columns = encoder.columns_)
new_data[new_data == False] = 0
new_data[new_data == True] = 1
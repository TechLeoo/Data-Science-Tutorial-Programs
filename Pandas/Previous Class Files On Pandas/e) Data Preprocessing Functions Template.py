# -*- coding: utf-8 -*-
"""
Created on Thu Apr 20 10:18:27 2023

@author: lEO
"""
import warnings
import numpy as np
import pandas as pd

warnings.filterwarnings("ignore")

# (1) Open our CSV file
dataset = pd.read_csv('Data.csv', delimiter = ',')

# (2) Performs Descriptive Statistics
des_stat = dataset.describe(include = 'all')

# (3) EDA
check_null = dataset.isnull()
dataset.info()

# (3) Selecting Columns
y = dataset.iloc[:, 3]
y1 = dataset.loc[:, 'Purchased']

x = dataset.iloc[:, [1, 2]]
x1 = dataset.iloc[:, 1:-1]
x2 = dataset.loc[:, ['Age', 'Salary']]

# (4) Creating New Columns From Existing
new_data = dataset.assign(salary_10years = dataset.iloc[:, 2] * 10)
new_data1 = dataset.assign(salary_10years = 'Man')
new_data2 = dataset.assign(salary_10years = 1)

# (5) Sorting Columns
sort = dataset.sort_values('Salary', ascending = False)

# (6) Pivot Table

# (7) Transpose
trans_data = dataset.T

# (8) Fixing Categorical Data
one_hot = pd.get_dummies(dataset[['Country']])



# P A N D A S   S Q L 
# (1) Doing SQL with Pandas
get = dataset.query('Age < 40 or Salary == 72000')
get_head = get.head()

# (2) Using GroupBy
frame = dataset.groupby(['Country'], dropna = True).count()
frame1 = dataset.groupby(['Country']).sum()
frame2 = dataset.groupby(['Country']).mean()



# O T H E R   F U N C T I O N S 
# Remember to always look up your documentation 
# a) dataset.rename() #Rename Columns and Index
# b) dataset.merge()  #Merge 2 Dataset
# c) dataset.to_csv() #Turn Files to an Exported CSV
# d) dataset.dropna()
# e) dataset.drop()
# f) dataset.fillna()
# g) dataset.sample()









# -*- coding: utf-8 -*-
"""
Created on Fri Nov 10 22:44:13 2023

@author: lEO
"""

import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
import scipy as sp
import statsmodels.api as sms

np.random.seed(23)
dataset = pd.DataFrame(np.round(np.random.normal(loc = 50, scale = 7, size = (2000, 5))), columns = ["Column1", "Column2", "Column3", "Column4", "Column5"])

# Descriptive Stats
descriptive_stats = sp.stats.describe(dataset, axis = 0, nan_policy = "omit")
print(descriptive_stats)

# # REMOVING OUTLIERS ---> METHOD 1
scaler = StandardScaler()
data = pd.DataFrame(scaler.fit_transform(dataset), columns = ["Column1", "Column2", "Column3", "Column4", "Column5"])

removed_outliers1 = data[(data < 3) & (data > -3)].dropna() # You can adjust it from 3. You can use -2.5 to 2.5

# # REMOVING OUTLIERS ---> METHOD 2
# removed_outliers2 = sp.stats.zscore(dataset)
# removed_outliers2 = removed_outliers2[(removed_outliers2 < 3) & (removed_outliers2 > -3)].dropna()

# REMOVING OUTLIERS ---> METHOD 3
# scaler = StandardScaler()
# data = pd.DataFrame(scaler.fit_transform(dataset), columns = ["Column1", "Column2", "Column3", "Column4", "Column5"])

# removed_outliers3 = data.where(data < 3).where(data > -3).dropna()
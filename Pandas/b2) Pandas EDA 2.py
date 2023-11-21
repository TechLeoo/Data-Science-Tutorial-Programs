# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 15:16:00 2023

@author: lEO
"""

dataset = 'INSERT THE LOCATION OF YOUR DATASET HERE'

# (3) EDA
head = dataset.head()
dataset.info()
descriptive_statistics = dataset.describe()
check_null = dataset.isnull()

# Exploring the DIFFERENT Column
info = dataset[['INSERT A COLUMN TO EXPLORE']]
mean_info = info.mean()
mode_info = info.mode()
median_info = info.median()
variance_info = info.var()

# Exploring the DIFFERENT Column
info1 = dataset[['INSERT A COLUMN TO EXPLORE']]
mean_info1 = info1.mean()
mode_info1 = info1.mode()
median_info1 = info1.median()
variance_info1 = info1.var()
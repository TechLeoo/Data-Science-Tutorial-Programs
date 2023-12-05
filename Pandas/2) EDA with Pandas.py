# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 20:54:31 2023

@author: lEO
"""

# 1) IMPORT LIBRARIES
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt # Visualization tool
import seaborn as sns # Visualization tool
import warnings

# DEAL WITH WARNINGS
warnings.filterwarnings("ignore")

# (2) GET THE DATASET
dataset1 = pd.read_csv("ds_salaries.csv")
dataset2 = pd.read_csv("50_Startups.csv")
dataset3 = pd.read_csv("laliga21-22.csv")
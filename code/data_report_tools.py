#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd

def cleaning_data(df):
    """
    Reports on missing data and duplicated rows in the data frame.
    
    Parameters:
    - df: pandas data frame to be analyzed.
    
    Returns:
    - A report of missing data counts and the number of duplicated rows.
    """
    missing_values = df.isnull().sum()
    print("Missing Values per Column:")
    print(missing_values[missing_values > 0])  
    
    duplicated_rows = df.duplicated().sum()
    print("\nNumber of Duplicated Rows:", duplicated_rows)


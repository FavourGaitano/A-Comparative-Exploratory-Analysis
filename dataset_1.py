# -*- coding: utf-8 -*-
"""Dataset 1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1MoREsml9TKuRYEIGckmdwoZ3Dhjf4fkr
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math
import statistics as stats
import seaborn as sns
from statistics import mean, mode, median, stdev

df =pd.read_csv('GDP-per-capita.csv')
df

df.columns

# drop columns 'indicator code', 'indicator name'
df.drop(['Indicator Name', 'Indicator Code'], axis=1, inplace=True)

df

df.info()

# drop rows with missing value
df.dropna(inplace=True)
df

# Drop columns from 1960 to 2000
cols_to_drop = [str(i) for i in range(1960, 2000)]
df.drop(columns=cols_to_drop, inplace=True, errors='ignore')
df

df.info()

df.columns

#check for missing values for years 2000 to 2021
missing_years = []
for year in range(2000, 2022):
    if str(year) not in df.columns:
        missing_years.append(year)
if len(missing_years) > 0:
    print(f"Missing values for years: {missing_years}")
    # drop rows with missing values or fill in missing values

# melt columns 2000 to 2021 into a new column called 'year'
df = pd.melt(df, id_vars=['Country Name','Country Code'], value_vars=[str(year) for year in range(2000, 2022)], var_name='year', value_name='GDP_value')

# convert year column to datetime format
df['year'] = pd.to_datetime(df['year'])

df

df.columns

#removing the data time format and coverting to int
df['year'] = df['year'].dt.year.astype(int)

df

df.rename(columns={'Country Name':'Country'}, inplace=True)

df

#Exporting the data in csv file
df.to_csv('GDP-per-capita1.csv', index = False)


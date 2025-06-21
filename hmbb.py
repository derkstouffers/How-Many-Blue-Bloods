# Deric Shaffer
# STAT371 - Final Project
# Purpose - Determine how many players from blue blood schools it took for an NBA team to be champions per year
#   As of right now, data is from NBA Champions from 1995-2023

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Data sourced from Basketball-Reference.com
# Website: https://www.basketball-reference.com/
# Basketball-Reference is a comprehensive online repository providing detailed basketball statistics.
# The data compiled here is for educational and analytical purposes.

# read in csv file
data = pd.read_csv('1995to2023.csv')

# deal with the empties that are international/drafted out of high school players
data['College'].fillna('international/high-school', inplace=True)

# blue blood schools
blue_bloods = ['Kentucky', 'Kansas', 'UNC', 'Duke']

# key = value --> year = # of blue blood players
hashmap = {year: 0 for year in data['Year'].unique()}

for _, row in data.iterrows():
    # check if college is a blue-blood school
    if row['College'] in blue_bloods:
        hashmap[row['Year']] += 1

# double check it worked/populated hashmap, and reverse years order from descending to ascending
ascending_years = dict(reversed(hashmap.items()))
print(ascending_years)

# get outliers
print(f'outliers = {[year for year, count in ascending_years.items() if count == 0]}')
print(f'highest = {max(ascending_years, key=ascending_years.get)}')

# plot 'bell curve' graph
plt.figure(figsize=(10, 6))
plt.bar(ascending_years.keys(), ascending_years.values(), color='blue', alpha=0.7, align='center')
plt.title('Blue Blood Players per Year (1995 - 2023)')
plt.xlabel('Year')
plt.ylabel('Number of Players from Blue Blood Colleges')
plt.grid(True)
plt.show()

# cumulative distribution function
cumulative_sum = np.cumsum(list(ascending_years.values()))
total_players = sum(ascending_years.values())
cumulative_probability = cumulative_sum / total_players

# plot CDF
plt.figure(figsize=(10, 6))
plt.step(ascending_years.keys(), cumulative_probability, where='mid', color='blue')
plt.title('Cumulative Distribution Function (1995 - 2023)')
plt.xlabel('Year')
plt.ylabel('Cumulative Probability')
plt.grid(True)
plt.show()

# determine expected value
how_many = np.mean(list(ascending_years.values()))
print(f'How many Blue Bloods does it take to screw in a lightbulb? It takes {how_many}.')
# round down to 1 or make a joke where it is one and a player who transferred to one during their college career

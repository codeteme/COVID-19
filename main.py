import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# for latex equations
from IPython.display import Math, Latex
# for displaying images
from IPython.core.display import Image

from numpy import random

# import os
# path = 'csse_covid_19_data/csse_covid_19_time_series/'
# csvs = [x for x in os.listdir(path) if x.endswith('.csv')]

# create a dictionary for all the files
# d = {}
# for file_name in csvs:
#     file_name = file_name.strip()
#     print(file_name)
# #    d[file_name] = pd.read_csv(file_name)

# define a function that takes in country name as an argument and returns a complete dataframe of that coutnry
# the dataframe should include confimed, recovered, and death counts

df_confirmed = pd.read_csv('csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv')
df_deaths = pd.read_csv('csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv')
df_recovered = pd.read_csv('csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_recovered_global.csv')

# choose Ethiopia row from dataframe
df_confirmed_eth = df_confirmed[df_confirmed['Country/Region'] == 'Ethiopia']
df_deaths_eth = df_deaths[df_deaths['Country/Region'] == 'Ethiopia']
df_recovered_eth = df_recovered[df_recovered['Country/Region'] == 'Ethiopia']



# replace missing values with 0
df_confirmed_eth = df_confirmed_eth.fillna(0)
df_deaths_eth = df_deaths_eth.fillna(0)
df_recovered_eth = df_recovered_eth.fillna(0)

# transpose the dataframe to construct a new one
df_confirmed_eth = df_confirmed_eth.transpose()
df_deaths_eth = df_deaths_eth.transpose()
df_recovered_eth = df_recovered_eth.transpose()

df_deaths_transpose = df_deaths.transpose()
df_deaths_transpose = df_deaths_transpose.iloc[4: ]

# add a column which is mean of all other columns values
df_deaths_transpose['average'] = df_deaths_transpose.mean(axis=1)

# change dtype to integer
df_deaths_transpose['average'] =  df_deaths_transpose['average'].astype(int)

# print(df_deaths_transpose)

# Reset index - convert index to column
df_confirmed_eth.reset_index(level=0, inplace=True)
df_deaths_eth.reset_index(level=0, inplace=True)
df_recovered_eth.reset_index(level=0, inplace=True)

# change column header names
df_confirmed_eth.columns = ['date', 'confirmed']
df_deaths_eth.columns = ['date', 'deaths']
df_recovered_eth.columns = ['date', 'recovered']

# drop unncessary values like Lat and Long
df_confirmed_eth = df_confirmed_eth.iloc[4: ]
df_deaths_eth = df_deaths_eth.iloc[4: ]
df_recovered_eth = df_recovered_eth.iloc[4: ]

# create final dataframe
eth_df = pd.DataFrame(columns=['confirmed', 'recovered', 'deaths', 'date'])
# eth_df['country'].fillna(0, inplace=True) # fill empty values in eth_df['country'] with "Ethiopia"

# populate the dataframe and change dtype 
eth_df['date'] = df_confirmed_eth['date']
eth_df['date'] = pd.to_datetime(eth_df['date'])
eth_df['confirmed'] = df_confirmed_eth['confirmed'].astype(int)
eth_df['deaths'] = df_deaths_eth['deaths'].astype(int)
eth_df['recovered'] = df_recovered_eth['recovered'].astype(int)

# homogenize the index values to copy column from one dataframe to another
eth_df.index = df_deaths_transpose.index
#assign the columns
# eth_df['global deaths average'] = df_deaths_transpose['average']

# # simple plot of all columns - ethiopiaßß
# eth_df.plot(x="date", y=['confirmed', 'recovered', 'deaths'])
# plt.ylabel('counts')
# plt.title('Ethiopia - Covid-19 Trend Analysis')
# plt.xticks(rotation=90)
# plt.show()

# lamba is total number of events divided by number of units a.k.a mean
# confirmed cases per day - I took the mean
lambda_eth = df_confirmed_eth['confirmed'].mean()

sns.set(color_codes = True)
sns.set(rc={'figure.figsize': (5, 5)})

# import poisson  distribution 
from scipy.stats import poisson

# # plot poisson distribution
# _ = sns.distplot(random.poisson(lam=lambda_eth, size=1000), hist=False, label='poisson')
# plt.xlabel('confirmed cases(events)')
# plt.ylabel('probability of event')
# plt.show() 




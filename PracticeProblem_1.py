#Use pandas to load chicago.csv into a dataframe,
#and find the most frequent hour when people start traveling.
#There isn't an hour column in this dataset,
#but you can create one by extracting the hour from the "Start Time" column.
#To do this, you can convert "Start Time" to the datetime datatype
# using the pandas to_datetime() method and extracting properties such as the hour

import pandas as pd

filename = 'chicago.csv'

# load data file into a dataframe
df = pd.read_csv('chicago.csv')
print(df.head())
print()

# convert the Start Time column to datetime
df['Start Time'] = pd.to_datetime(df['Start Time'])
print(df['Start Time'].dtype)
print()

# extract hour from the Start Time column to create an hour column
df['hour'] = df['Start Time'].dt.hour
print()

# find the most common hour (from 0 to 23)
popular_hour = df['hour'].mode()[0]

print()
print('Most Frequent Start Hour:', popular_hour)

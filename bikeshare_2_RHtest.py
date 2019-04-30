import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')

    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

    city = ''
    while city not in CITY_DATA:
        city = input("\nEnter city name to explore data: ").lower()
        if city not in CITY_DATA:
            print("\nSorry! We don't track {}. Please insert 'chicago', 'new york city', or 'washington' only\n".format(city))
        else:
            print("\nWe have {} in our data set!".format(city))

    # TO DO: get user input for month (all, january, february, ... , june)
    months = {'all', 'january', 'february', 'march', 'april', 'may', 'june'}
    month = ''
    while month not in months:
        month = input("\nWhich month would you like to filter by? You can select any month in the first half of the year, or select 'all': ").lower()
        if month not in months:
            print("\nTry again! Please choose from one of the following {}".format(months))
        else:
            print("\nYou selected {}!".format(month))

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    days = {'all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday'}
    day = ''
    while day not in days:
        day = input("Which day of the week? Please enter the full name for the day e.g. sunday, or select all: ").lower()
        if day not in days:
            print("\nTry Again! Don't forget to spell day of the week correctly, or select all!")
        else:
            print("\n You selected {}!".format(day))

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour
    df['month_name'] = df['Start Time'].dt.strftime('%B')

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        print(df.head())

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()

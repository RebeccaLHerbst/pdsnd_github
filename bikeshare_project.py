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

    print('-'*20)
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
    df['month_name'] = df['Start Time'].dt.strftime('%B')
    df['start_hour'] = df['Start Time'].dt.hour


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


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    popular_month = df['month_name'].mode()[0]
    print("\nThe most popular month for bike rentals is {}.".format(popular_month))

    # TO DO: display the most common day of week
    popular_day = df['day_of_week'].mode()[0]
    print("\nThe most popular day of the week for bike rentals is {}.".format(popular_day))

    # TO DO: display the most common start hour
    popular_start_hour = df['start_hour'].mode()[0]
    print("\nThe most popular hour of the day for bike rentals is {}.".format(popular_start_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*20)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print("\nThe most popular start station is {}.".format(popular_start_station))

    # TO DO: display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print("\nThe most popular end station is {}.".format(popular_end_station))

    # TO DO: display most frequent combination of start station and end station trip
    df['Popular Start-End Combo'] = (df['Start Station'] + " to " + df['End Station'])
    popular_start_end_combo = df['Popular Start-End Combo'].mode()[0]
    print("\nThe most popular station combination is {}.".format(popular_start_end_combo))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*20)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = round(df['Trip Duration'].sum())
    print("\nThe total travel time was {} seconds.".format(total_travel_time))

    # TO DO: display mean travel time
    average_travel_time = round(df['Trip Duration'].mean())
    print("\nThe average travel time was {} seconds.".format(average_travel_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*20)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print("\nThe number are user types are as follows:\n")
    print(user_types)
    print()


    # TO DO: Display counts of gender
    if 'Gender' in df.columns:
        gender = df['Gender'].value_counts()
        print("\nThe number of rentals per gender are as follows:\n")
        print(gender)
        print()
    else:
        print("\nSorry, this city doesn't have gender data.")
        print()


    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        earliest_birthyear = int(np.nanmin(df['Birth Year']))
        print("\nFor bike renters, {} is the earliest birth year.".format(earliest_birthyear))
        recent_birthyear = int(np.nanmax(df['Birth Year']))
        print("\nFor bike renters, {} is the most recent birth year.".format(recent_birthyear))
        most_common_birthyear = int((df['Birth Year']).mode()[0])
        print("\nFor bike renters, {} is the most common birth year.".format(most_common_birthyear))
    else:
        print("\nSorry, this city doesn't have birth year data.")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*20)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        more_data = input('\nWould you like to see some data? Enter yes or no.\n')
        if more_data.lower() == 'yes':
            print(df.head())
            print()

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()

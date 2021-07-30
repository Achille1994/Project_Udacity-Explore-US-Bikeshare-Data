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
    cities=['chicago','new york city','washington']
    while True:
        city=input('Which of these cities would you want to explore: Chicago, New York city, Washington? ').lower()
        if city not in cities:
            print('Invalid city.Please enter a valid city: Chicago, New York city, or Washington ')
        else:
            break

    # TO DO: get user input for month (all, january, february, ... , june)
    months = ['january', 'february', 'march', 'april', 'may', 'june']
    month=""
    while True:
        if month !="all":
            month=input('which month would you want to filter: January, Feburary, March, April, May or June? ').lower()
            break


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    day=""
    while True:
        if day !="all":
            day=input('Which day would you want to filter: Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, sunday? ').lower()
            break

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
    df=pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

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
    """Displays statistics on the most frequent times of travel.
     Args:
        (DataFrame) df - Pandas DataFrame containing city data filtered by month and day
    """

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()


    # TO DO: display the most common month
    popular_month=df["month"].mode()[0]
    print("popular_month: ", popular_month)


    # TO DO: display the most common day of week
    popular_day_of_week = df['day_of_week'].mode()[0]
    print('popular day of week: ', popular_day_of_week)


    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print('popular hour: ', popular_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip.
     Args:
        (DataFrame) df - Pandas DataFrame containing city data filtered by month and day
    """

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station= df['Start Station'].mode()[0]
    print("most commonly used start station: ",popular_start_station)


    # TO DO: display most commonly used end station
    popular_end_station= df['End Station'].mode()[0]
    print("most commonly used end station: ",popular_end_station)


    # TO DO: display most frequent combination of start station and end station trip
    df['combination_station']=df['Start Station'] + " " + df['End Station']
    combination_station= df['combination_station'].mode()[0]
    print("most frequent combibation of start station and end station trip: ", combination_station)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel=df["Trip Duration"].sum()
    print('total travel time: ', total_travel)



    # TO DO: display mean travel time
    average_travel=df["Trip Duration"].mean()
    print('mean travel time: ', average_travel)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users.
     Args:
        (DataFrame) df - Pandas DataFrame containing city data filtered by month and day
    """

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    counts_user=df['User Type'].value_counts()
    print("counts of user types: ",counts_user)


    # TO DO: Display counts of gender
    if 'Gender' in df:
        counts_gender=df['Gender'].value_counts()
        print("counts of gender : ",counts_gender)
    else:
        print( "There is no gender information in this city")


    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df:
        earlisest_year=df["Birth Year"].min()
        recent_year=df["Birth Year"].max()
        common_year=df["Birth Year"].mode()[0]
        print("earliest year of birth: ", earlisest_year)
        print("recent year of birth:   ", recent_year)
        print("most common year of birth: ", common_year)
    else:
        print( "There is no Birth Year information in this city")



    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df):
    view_data=input('\nWould you like to view 5 rows of individual trip data ? Enter yes or no\n').lower()
    start_loc=0
    while view_data=="yes":
        print(df.iloc[0:start_loc+5])
        start_loc +=5
        view_display=input("Do you wish to continue ? : ").lower()
        if view_display=="no":
            break


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()

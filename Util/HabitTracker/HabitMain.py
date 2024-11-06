#pip install pandas
#pip install tabulate

import pandas as pd
from tabulate import tabulate
from datetime import datetime
from HabitTracker import track_habit, Habit

def main():
    # Habits
    habits: list[Habit] = [
        track_habit('Coffee', datetime(2023,5,6,8), cost=1, minutes_used=5),
        track_habit('Wasting time', datetime(2024,10,29,6), cost=100, minutes_used=60 * 12)
    ]

    # Creates a Dataframe
    df = pd.DataFrame(habits)

    # Create a nice table
    print(tabulate(df, headers='keys', tablefmt='psql'))


if __name__ == '__main__':
    main()
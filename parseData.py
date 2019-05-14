"""
    File name: parseData.py
    Author: Kurtis Davidson
    Date created: 5/3/2019
    Date last modified: 5/13/2019
    Python Version: 3.7.3
"""

import pandas as pd

# Parses csv file and returns a dataframe object
def create_table():
    # Parses csv to dataframe object
    df = pd.read_csv('sampleData.csv', sep='|')

    # Formats the columns into their respective data types
    df['DATE'] = pd.to_datetime(df['DATE'], format='%Y-%m-%d').dt.date
    df['VIEW_TIME'] = pd.to_datetime(df['VIEW_TIME'], format='%H:%M').dt.time
    # Round REV up to 2 decimal places for cents
    df['REV'] = df['REV'].round(decimals=2)

    # Sets records to be unique by STB, TITLE, and DATE
    df = df.drop_duplicates(subset=['STB', 'TITLE', 'DATE'])
    return df

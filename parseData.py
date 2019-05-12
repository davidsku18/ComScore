import pandas as pd
import os.path
import sqlite3

# Connecting to sqlite3 and storing into main memory
conn = sqlite3.connect(':memory:')
cur = conn.cursor()

# Parses csv file and creates table
def create_table():
    buffer = ''
    # Parses csv to dataframe object
    df = pd.read_csv('sampleData.csv', sep='|')

    # Formats the columns into their respective data types
    df['DATE'] = pd.to_datetime(df['DATE'], format='%Y-%m-%d').dt.date
    df['VIEW_TIME'] = pd.to_datetime(df['VIEW_TIME'], format='%H:%M').dt.time
    # Round REV up to 2 decimal places for cents
    df['REV'] = df['REV'].round(decimals=2)

    # Sets records to be unique by STB, TITLE, and DATE
    df = df.drop_duplicates(subset=['STB', 'TITLE', 'DATE'])

    # Dataframe object to sql database, if exists then overwrite
    df.to_sql(name='movie', con=conn, if_exists='replace')

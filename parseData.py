import pandas as pd
import os.path
import sqlalchemy

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "movie.db")

# Connecting to sqlite3
engine = sqlalchemy.create_engine('sqlite:///' + db_path)

# Parses csv file and creates table
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

    # Dataframe object to sql database, if exists then overwrite
    df.to_sql(name='movie', con=engine, if_exists='replace')

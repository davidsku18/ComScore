import pandas as pd
import os.path
import sqlite3
import argparse

# Connecting to sqlite3 and storing into main memory
conn = sqlite3.connect(':memory:')

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
    df.to_sql(name='movie', con=conn, if_exists='replace')

create_table()
parser = argparse.ArgumentParser(description='Process queries')
parser.add_argument("-s", "--SELECT", nargs='+',
            help="Selects the specified column")
parser.add_argument("-o", "--ORDER", nargs='+',
            help="The column(s) that the data will be ordered with")
parser.add_argument("-f", "--FILTER", nargs='+',
            help="Finds the specified data")
args = parser.parse_args()

# Gets the SELECT arguments
def get_select():
    if(args.SELECT is not None):
        select = ', '.join(args.SELECT)
        select = 'SELECT ' + select
        return select
    else:
        select = 'SELECT *'
        return select

# Gets the ORDER arguments
def get_order():
    if(args.ORDER is not None):
        order = ', '.join(args.ORDER)
        order = 'ORDER BY ' + order
        return order
    else:
        order = ''
        return order

# Gets the FILTER arguments
def get_filter():
    if(args.FILTER is not None):
        filter = filter = ''.join(args.FILTER).split('=')
        filter = 'WHERE ' + filter[0] + ' = ' + "'" + filter[1] + "'"
        return filter
    else:
        filter = ''
        return filter

print(pd.read_sql_query(sql=get_select() + ' FROM movie ' + get_filter() + get_order() + ";", con=conn))

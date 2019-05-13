import pandas as pd
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
        select = 'SELECT '
        for arg in args.SELECT:
            if(':' in arg):
                select_with_arg = ''.join(arg).split
                select_with_arg = ''
            else:
                select = select + ', '.join(args.SELECT)
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
        filter = 'WHERE '
        separate_args = ''.join(args.FILTER).split(',')
        for i, arg in enumerate(separate_args):
            if(i is not len(separate_args) and i is not len(separate_args) - 1):
                if('REV' not in arg):
                    filter_argument = ''.join(arg).split('=')
                    print(filter_argument)
                    filter = filter + filter_argument[0] + " = " + "'" + filter_argument[1] + "'" + ' AND '
                else:
                    filter = filter + arg + ' AND '
            elif(i is len(separate_args)-1):
                if('REV' not in arg):
                    filter_argument = ''.join(arg).split('=')
                    print(filter_argument)
                    filter = filter + filter_argument[0] + " = " + "'" + filter_argument[1] + "' "
                else:
                    filter = filter + arg + ' '
        return filter
    else:
        filter = ''
        return filter

print('SQL QUERY: ' + get_select() + ' FROM movie ' + get_filter() + get_order() + ";")
print(pd.read_sql_query(sql=get_select() + ' FROM movie ' + get_filter() + get_order() + ";", con=conn))

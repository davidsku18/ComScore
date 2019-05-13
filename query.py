import argparse
import pandas as pd
import parseData
import sqlite3

conn = sqlite3.connect(':memory:')
# Creates the table and converts to sql database, if exists then overwrites
parseData.create_table().to_sql(name='movie', con=conn, if_exists='replace')
parser = argparse.ArgumentParser(description='Process queries')

# The flags that can be used
parser.add_argument("-s", "--SELECT", nargs='+', help="Selects the specified column")
parser.add_argument("-o", "--ORDER", nargs='+', help="The column(s) that the data will be ordered with")
parser.add_argument("-f", "--FILTER", nargs='+', help="Finds the specified data")
args = parser.parse_args()

# Gets the SELECT arguments
def get_select():
    if(args.SELECT is not None):
        select = 'SELECT '
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
        # Iterate through the list to find our filter arguments
        for i, arg in enumerate(separate_args):
            # Adds AND so that filters can be combined
            if(i is not len(separate_args) and i is not len(separate_args) - 1):
                if('REV' not in arg):
                    filter_argument = ''.join(arg).split('=')
                    filter = filter + filter_argument[0] + " = " + "'" + filter_argument[1] + "'" + ' AND '
                else:
                    filter = filter + arg + ' AND '
            # Last element of list must not have an AND
            elif(i is len(separate_args)-1):
                if('REV' not in arg):
                    filter_argument = ''.join(arg).split('=')
                    filter = filter + filter_argument[0] + " = " + "'" + filter_argument[1] + "' "
                else:
                    filter = filter + arg + ' '
        return filter
    else:
        # Empty filter
        filter = ''
        return filter

print('SQL QUERY: ' + get_select() + ' FROM movie ' + get_filter() + get_order() + ";")
# Applies the query and prints the table
print(pd.read_sql_query(sql=get_select() + ' FROM movie ' + get_filter() + get_order() + ";", con=conn))
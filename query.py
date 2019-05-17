"""
    File name: query.py
    Author: Kurtis Davidson
    Date created: 5/13/2019
    Date last modified: 5/16/2019
    Python Version: 3.7.3
"""

import argparse
import pandas as pd
import parseData

# Creates the dataframe object
df = parseData.create_table()
parser = argparse.ArgumentParser(description='Process queries')

# The flags to specify each query
parser.add_argument("-s", "--SELECT", nargs='+', help="Selects the specified column")
parser.add_argument("-o", "--ORDER", nargs='+', help="The column(s) that the data will be ordered with")
parser.add_argument("-f", "--FILTER", nargs='+', help="Finds the specified data")
parser.add_argument("-g", "--GROUP", nargs='+', help="Groups the data in the specified manner")
args = parser.parse_args()

# Pases in a dataframe, parses the args and manipulates the dataframe
def parse_args(df):
    # Parses SELECT arguments and selects the columns for the dataframe
    if (args.SELECT):
        column = ''.join(args.SELECT).split(',')
        df = df[column]
    # Parses the ORDER arguments to order the data in the dataframe
    if (args.ORDER):
        order = ''.join(args.ORDER).split(',')
        df = df.sort_values(by=order)
    # Parses the FILTER arguments to filter the data in the dataframe
    if (args.FILTER):
        filter = ''
        arg_list = ''.join(args.FILTER).split(',')
        for i, arg in enumerate(arg_list):
            # Adds an and to chain multiple filters together
            if(i is not len(arg_list) and i is not len(arg_list) - 1):
                # Need to change "=" to "=="
                if('=' in arg):
                    filter_arg = arg.split('=')
                    filter =  filter_arg[0] + '==' + "'" + filter_arg[1] + "' and "
                # Take filter as is and add to filter
                else:
                    filter = arg + " and "
            # Filter is either the last or the only one in the list, therefore,
            # "and" doesn't need to be added
            else:
                # Need to change "=" to "=="
                if('=' in arg):
                    filter_arg = arg.split('=')
                    filter = filter + filter_arg[0] + '==' + "'" + filter_arg[1] + "'"
                # Take filter as is and add to filter
                else:
                    filter = filter + arg
        df = df.query(filter)
    # Parses the GROUP arguments to group the data by in the dataframe
    if (args.GROUP):
        group = ''.join(args.GROUP).split(',')
        df = df.groupby(group).first()
    return df

# Shows the entered arguments
def print_args():
    for arg in vars(args).items():
        print(arg)

# Prints the queried table
def print_table(df):
    print_args()
    print(parse_args(df))

print_table(df)

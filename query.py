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

# Creates the table and converts to sql database, if exists then overwrites
df = parseData.create_table()
parser = argparse.ArgumentParser(description='Process queries')

# The flags that can be used
parser.add_argument("-s", "--SELECT", nargs='+', help="Selects the specified column")
parser.add_argument("-o", "--ORDER", nargs='+', help="The column(s) that the data will be ordered with")
parser.add_argument("-f", "--FILTER", nargs='+', help="Finds the specified data")
parser.add_argument("-g", "--GROUP", nargs='+', help="Groups the data in the specified manner")
args = parser.parse_args()

def parse_args(df):
    if (args.SELECT is not None):
        column = ''.join(args.SELECT).split(',')
        df = df[column]
    if (args.ORDER is not None):
        order = ''.join(args.ORDER).split(',')
        df = df.sort_values(by=order)
    if (args.FILTER is not None):
        filter = ''
        arg_list = ''.join(args.FILTER).split(',')
        for i, arg in enumerate(arg_list):
            if(i is not len(arg_list) and i is not len(arg_list) - 1):
                if('=' in arg):
                    filter_arg = arg.split('=')
                    filter =  filter_arg[0] + '==' + "'" + filter_arg[1] + "' and "
                else:
                    filter = arg + " and "
            else:
                if('=' in arg):
                    filter_arg = arg.split('=')
                    filter = filter + filter_arg[0] + '==' + "'" + filter_arg[1] + "'"
                else:
                    filter = filter + arg
        df = df.query(filter)
    if (args.GROUP is not None):
        group = ''.join(args.GROUP).split(',')
        df = df.groupby(group).first()
    return df

print(parse_args(df))

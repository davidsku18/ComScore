# ComScore

Installation required:
pandas : 'pip3 install pandas'

This program parses and queries a given csv file separated by '|' and utilizes sqlite3
To run the program: python3 query.py
 - This will parse the sampleData.csv and save the datastore to memory
 - Data is unique by STB, TITLE, and DATE
 - The table will then be printed to the screen

- To query the data further, flags can be used:
  - "-h" or "--help" to show the flags available to use and what they do:
    - ex: "python3 parseData.py -h"
  - "-s" or "--SELECT" followed by the columns to select columns to be displayed:
    - ex: "python3 query.py -s TITLE, DATE, REV"
  - "-o" or "--ORDER" to select the order in which the data is displayed:
    - ex: "python3 query.py -s TITLE, DATE, REV -o REV"
  - "-f" or "--FILTER" to filter the data as specified
    - ex: "python3 query.py -s TITLE, DATE, REV -f REV>4.0"
    - ex: "python3 query.py -s TITLE, DATE, REV -f DATE=2014-04-02,REV>=4.0"
    - When filtering text with a space, quotes must surround the text so that the words aren't taken as multiple arguments:
      - ex: "python3 query.py -s TITLE, DATE, REV -f TITLE='the matrix'"
  - "-g" or "--GROUP" to group the data as specified
    - ex: "python3 query.py -s TITLE, DATE, REV, -g TITLE"

- To query the data using aggregate functions, use the selected column followed by a ":" and then the function:
  - MIN: select the minimum value from a column
    - ex: "python3 query.py -s TITLE, DATE, REV:min"
  - MAX: select the maximum value from a column
    - ex: "python3 query.py -s TITLE, DATE, REV:max"
  - SUM: select the summation of all values in a column:
    - ex: "python3 query.py -s TITLE, DATE, REV:sum"
  - COUNT: count the distinct values in a column
    - ex: "python3 query.py -s TITLE, DATE, REV:count"
  - COLLECT: collect the distinct values in a column (collect function does not exist in sqlite3 so DISTINCT needs to be added)
    - ex: "python3 query.py -s TITLE, DATE, 'DISTINCT REV':count"

- To utilize advanced filters, '"' (double quotes) must be used around the filter argument while "'" (single quotes) must be used around text within the argument:
  - ex: python3 query.py -f "STB='stb1' AND TITLE='the hobbit' OR TITLE='the matrix'"

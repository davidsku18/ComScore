# ComScore

Installation required:
pandas : 'pip3 install pandas'

This program parses and queries a given csv file separated by '|'
To run the program: python3 query.py
 - This will parse the sampleData.csv and save the datastore to memory
 - Data is unique by STB, TITLE, and DATE
 - The data will then be printed to the screen
 - To query the data further, flags can be used:
    - '-s' or '--SELECT' followed by the columns to select columns to be displayed:
        - ex: 'python3 query.py -s TITLE, DATE, REV'
    - '-o' or '--ORDER' to select the order in which the data is displayed:
        - ex: 'python3 query.py -s TITLE, DATE, REV -o REV'
    - '-f' or '--FILTER' to filter the data by specified
        - ex: 'python3 query.py -s TITLE, DATE, REV -f REV>4.0'
        - ex: 'python3 query.py -s TITLE, DATE, REV -f DATE=2014-04-02,REV>=4.0'
    - '-h' or --help to show the flags available to use and what they do:
        - ex: 'python3 parseData.py -h'

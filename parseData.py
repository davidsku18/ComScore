import pandas as pd
import sqlite3

filepath = 'data.csv'

def create_table():
    # Parses csv to dataframe object
    df = pd.read_csv('sampleData.csv', sep='|')

    # Connecting to the sqlite3
    conn = sqlite3.connect('movie.db')
    c = conn.cursor()

    # Dataframe object to database
    df.to_sql(name = 'movie', con = conn, if_exists = 'replace')


def show_all():
    create_table()
    c.execute("SELECT * FROM movie").fetchall()

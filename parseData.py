import pandas as pd
import os.path
import sqlalchemy

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "movie.db")

# Parses csv to dataframe object
df = pd.read_csv('sampleData.csv', sep='|')
df['VIEW_TIME'] = pd.to_datetime(df['VIEW_TIME'], format='%H:%M').dt.time
df['DATE'] = pd.to_datetime(df['DATE'], format='%Y-%m-%d').dt.date

# Connecting to the sqlite3
engine = sqlalchemy.create_engine('sqlite:///' + db_path)

# Dataframe object to database
df.to_sql(name = 'movie', con = engine, if_exists = 'replace')

engine.execute("SELECT * FROM movie")

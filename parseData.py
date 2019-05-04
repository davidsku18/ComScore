import pandas

df = pandas.read_csv('sampleData.csv', sep='|', index_col='STB')
print(df)

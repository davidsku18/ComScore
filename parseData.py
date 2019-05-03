import csv

filepath = 'sampleData.csv'
csv.register_dialect('piper', delimiter='|', quoting=csv.QUOTE_NONE)

with open(filepath, "r") as csvfile:
    reader = csv.DictReader(csvfile, dialect='piper')
    for row in reader:
        print(row)
        print('\n')

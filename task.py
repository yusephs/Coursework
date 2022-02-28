import csv

with open ('data2.csv', 'r') as file:
    data = csv.reader(file, delimiter = '|')

    print(data)
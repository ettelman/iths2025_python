import csv

with open('data.csv', 'r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for line in reader:
        print(line)
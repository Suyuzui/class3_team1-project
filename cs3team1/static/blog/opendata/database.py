import csv
with open('ingredients.csv', 'r')as r:
    reader = csv.reader(r)
    for row in reader:
        print(row)
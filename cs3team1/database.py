import csv
with open('/static/blog/opendata/recipe.csv', 'r')as r:
    reader = csv.reader(r)
    for row in reader:
        print(row)
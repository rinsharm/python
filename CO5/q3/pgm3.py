import csv
list = []
with open('text.csv') as csvfile:
    fr = csv.reader(csvfile)

    for rows in fr:
       list.append(rows)

print(list)

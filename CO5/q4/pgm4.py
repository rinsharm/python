import csv
with open('fil2.csv', newline='') as csvfile:
 data = csv.DictReader(csvfile)
 for row in data:
   print(row['name'], row['rollno'])

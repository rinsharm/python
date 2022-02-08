import csv

mydict=[{'name':'rinsha','department':'cs','rollno':'120'},
        {'name':'john','department':'history','rollno':'121'},
        {'name':'karthik','department':'english','rollno':'122'}]

fields=['name','department','rollno']

with open('whoknows.csv','r+') as new_csvfile:

    writer = csv.DictWriter(new_csvfile,fieldnames=fields)

    writer.writeheader()

    writer.writerows(mydict)

    new_csvfile.close()
    
with open('whoknows.csv','r') as csvfile:

    read=csv.reader(csvfile)
    for rows in read:
        print(rows)

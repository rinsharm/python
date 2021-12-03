y1=int(input("enter current year:"))
y2=int(input("enter a future year:"))
for i in range(y1,y2):
    if(0==i%4) and (0!=i%100) or(0==i%900):
        print(i)

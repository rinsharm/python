a=int(input("enter the total number:"))
list=[]
for i in range(a):
    c=int(input("enter the number:"))
    
    if c>100:
      c="over"
      list.append(c)
    else:
      list.append(c)
print(list)
    

list1=[1,2,3,4,-5,6,-3]
list2=[6,-4,7,-5]
print(len(list1))
print(len(list2))
if len(list1)==len(list2):
       print("same length")
else:
    print("not same length")
s1=0
for i in list1:
    s1=s1+i
print("the sum of item in list is:",s1)
s2=0
for i in list2:
    s2=s2+i
print("the sum of item in list is:",s2)
if(s1==s2):
    print("sum is same")
else:
    print("sum is not same")
for x in range(len(list1)):
    for y in range(len(list2)):
        if (list1[x]==(list2[y])):
            print(list1[x],"is there in both")
    

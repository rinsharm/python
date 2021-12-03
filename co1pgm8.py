a=(input("enter the string"))
s=a[0]
a=a[1:]
a=a.replace(s,"$")
anew=s+a
print("the string is",anew)

fr=open("hello.txt","r")
print(fr.readlines())
fr.close()
fr1=open("hello.txt","r")
for line in fr1.readlines():
    print(line)
fr1.close()


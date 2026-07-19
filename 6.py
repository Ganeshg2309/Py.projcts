names=[]
f1=open("marks6.txt","r")
for i in range(0,26,1):
    s1=f1.readline()
    list1=s1.split(",")
    names.append(list1[0])
print(names)

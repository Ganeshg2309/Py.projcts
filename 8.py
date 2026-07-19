names=[]
english=[]
maths=[]
f1=open("marks6.txt","r")
for i in range(0,26,1):
    s1=f1.readline()
    list1=s1.split(",")
    names.append(list1[0])
    
    list2=list1[3].split(":")
    english.append(list2[1])

    list2=list1[4].split(":")
    maths.append(list2[1])
print(names)
print(english)
print(maths)

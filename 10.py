names=[]
english=[]
maths=[]
toppersEng=[]
toppersMat=[]
f1=open("marks6.txt","r")
for i in range(0,26,1):
    s1=f1.readline()
    list1=s1.split(",")
    names.append(list1[0])
    
    list2=list1[3].split(":")
    english.append(int(list2[1]))

    list2=list1[4].split(":")
    maths.append(int(list2[1]))
print(names)
print(english)
print(maths)
maxEng=max(english)
maxMat=max(maths)
print(maxEng)
print(maxMat)
for i in range(0,26,1):
    if english[i]==maxEng:
        toppersEng.append(names[i])
    if maths[i]==maxMat:
        toppersMat.append(names[i])
print(toppersEng,"are the toppers in english with marks",maxEng)
print(toppersMat,"are the toppers in maths with marks",maxMat)



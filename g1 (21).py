student = "Amar,M,E80BD46CS0001,English:74,Maths:90,Physics:86,Chemistry:78,Biology:60,PASS"
data=student.split(",")
print("name:",data[0])
total=0
for i in range(3,8):
    subject=data[i].split(":")
    print(subject[0],":",subject[1])
    total+=int(subject[1])
print()
print("total:",total)
print("average:",total/5)
#display student report

student = "Amar,M,E80BD46CS0001,English:74,Maths:90,Physics:86,Chemistry:78,Biology:60,PASS"
data=student.split(",")
print("single student report")
print("-"*20)
print("name:",data[0])
print("gender:",data[1])
print("usn:",data[2])
print()
total=0
for i in range(3,8):
    subject=data[i].split(":")
    marks=int(subject[1])
    total+=marks
    print(subject[0],":",marks)
print()
print("total:",total)
print("average:",total/5)
print("result:",data[8])

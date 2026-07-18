student = "Amar,M,E80BD46CS0001,English:74,Maths:90,Physics:86,Chemistry:78,Biology:60,PASS"
data=student.split(",")
for i in range(3,8):
    subject=data[i].split(":")
    name=subject[0]
    marks=int(subject[1])
    print(name,"=",marks)
#print subject name and marks together


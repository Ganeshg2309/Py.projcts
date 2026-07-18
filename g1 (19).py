student = "Amar,M,E80BD46CS0001,English:74,Maths:90,Physics:86,Chemistry:78,Biology:60,PASS"
data=student.split(",")
total=0
for i in range(3,8):
    marks=int(data[i].split(":")[1])
    total=total+marks
    average=total/5
print("total=",total)
print("average=",average)
#using for loop 

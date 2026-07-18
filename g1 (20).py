student = "Amar,M,E80BD46CS0001,English:74,Maths:90,Physics:86,Chemistry:78,Biology:60,PASS"
data=student.split(",")
lowest=int(data[3].split(":")[1])
for i in range(3,8):
    marks=int(data[i].split(":")[1])
    if marks<lowest:
        lowest=marks
print("lowest=",lowest)
#to print highest marks

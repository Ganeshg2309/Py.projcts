student = "Amar,M,E80BD46CS0001,English:74,Maths:90,Physics:86,Chemistry:78,Biology:60,PASS"
data=student.split(",")
english=int(data[3].split(":")[1])
maths=int(data[4].split(":")[1])
total=english+maths
print("english:",english)
print("maths:",maths)
print("total:",total)

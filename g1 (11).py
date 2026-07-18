student = "Amar,M,E80BD46CS0001,English:74,Maths:90,Physics:86,Chemistry:78,Biology:60,PASS"
data=student.split(",")
english=int(data[3].split(":")[1])
maths=int(data[4].split(":")[1])
physics=int(data[5].split(":")[1])
chemistry=int(data[6].split(":")[1])
biology=int(data[7].split(":")[1])
print(english)
print(maths)
print(physics)
print(chemistry)
print(biology)
#store all marks in variable


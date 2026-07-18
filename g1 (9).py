student = "Amar,M,E80BD46CS0001,English:74,Maths:90,Physics:86,Chemistry:78,Biology:60,PASS"
data=student.split(",")
english=data[3].split(":")
maths=data[4].split(":")
physics=data[5].split(":")
print(physics[0])
print(int(physics[1]))
#extracting math marks


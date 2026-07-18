student = "Amar,M,E80BD46CS0001,English:74,Maths:90,Physics:86,Chemistry:78,Biology:60,PASS"
data=student.split(",")
english=data[3].split(":")
maths=data[4].split(":")
physics=data[5].split(":")
biology=data[7].split(":")
print(biology[0])
print(int(biology[1]))
#extracting  biology marks


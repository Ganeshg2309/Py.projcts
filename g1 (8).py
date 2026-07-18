student = "Amar,M,E80BD46CS0001,English:74,Maths:90,Physics:86,Chemistry:78,Biology:60,PASS"
data=student.split(",")
english=data[3].split(":")
print("subject:",english[0])
marks=int(english[1])
print("marks:",marks)
print(type(marks))
#converting english marks to integer


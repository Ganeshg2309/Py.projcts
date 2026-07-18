student = "Amar,M,E80BD46CS0001,English:74,Maths:90,Physics:86,Chemistry:78,Biology:60,PASS"
data=student.split(",")
english=data[3]
subject_marks=english.split(":")
print("subject:",subject_marks[0])
print("marks:",subject_marks[1])
#NESTED SPLIT

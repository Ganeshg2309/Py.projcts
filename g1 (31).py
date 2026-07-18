student_data = "Amar,M,E80BD46CS0001,English:74,Maths:90,Physics:86,Chemistry:78,Biology:60,PASS"
data=student_data.split(",")
student={}
student["name"]=data[0]
student["gender"]=data[1]
student["usn"]=data[2]

student["english"]=int(data[3].split(":")[1])
student["maths"]=int(data[4].split(":")[1])
student["physics"]=int(data[5].split(":")[1])
student["chemistry"]=int(data[6].split(":")[1])
student["biology"]=int(data[7].split(":")[1])
student["result"]=data[8]
student["total"]=(student["english"]+student["maths"]+student["physics"]+student["chemistry"]+student["biology"])
student["average"]=student["total"]/5
for key in student:
    print(key,":",student[key])

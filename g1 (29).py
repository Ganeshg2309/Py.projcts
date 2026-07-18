student={}
student["name"]="amar"
student["gender"]="m"
student["usn"]="E80BD46CS0001"

student["english"]=74
student["maths"]=90
student["physics"]=86
student["chemistry"]=78
student["biology"]=60
student["total"]=388
student["average"]=77.6
print("student report")
print("-"*30)
for key in student:
    print(key,":",student[key])

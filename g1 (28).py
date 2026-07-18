student={}
student["english"]=74
student["maths"]=90
student["physics"]=86
student["chemistry"]=78
student["biology"]=60
student["total"]=(
    student["english"]
       +student["maths"]
       +student["physics"]
       +student["chemistry"]
       +student["biology"]
    )
student["average"]=student["total"] / 5
print(student)
print(student[5])

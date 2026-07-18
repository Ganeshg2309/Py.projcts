marks1=[]
file1=open("marks1.txt","r")
#file1=file1.read()
marks=file1.split(",")
for mark in marks:
    marks1.append(int(mark))
print(marks1)
highest=max(marks1)
print(highest)


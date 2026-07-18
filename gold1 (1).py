names1=[]
file1=open("names1.txt","r")
for line in file1:
    names1.append(line.strip(","))
print(names1)


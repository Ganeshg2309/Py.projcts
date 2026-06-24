file2=open("2.txt","r")
line=file2.readline()
start,end=line.split(",")
start=int(start)
end=int(end)
print(start,end)
file2.close()
for j in range(start,end+1):
    for i in range(1,11):
        print(str(j)+"*"+str(i)+"="+str(j*i))
    print()

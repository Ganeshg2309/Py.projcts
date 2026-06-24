file1=open("1.txt","r")
start=int(file1.readline())
end=int(file1.readline())
print(start,end)
for j in range(start,end+1):
    for i in range(1,11):
        print(str(j)+"*"+str(i)+"="+str(j*i))
    print()
    

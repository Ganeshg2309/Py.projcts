start=int(input(" enter first number "))
end=int(input("enter second number"))
filename=input("enter your filename:")
file1=open(filename,"w")
for j in range(start,end+1):
    for i in range(1,11):
        file1.write(str(j)+"*"+str(i)+"="+str(j*i))
        file1.write("\n")
    print("\n")        
    file1.write( "\n" )
file1.close()
print("output saved in ",filename)


start=input("enter first number")
end=input("enter second number")
for j in range(start,end):
    for i in range(1,11):
        print(str(j)+"*"+str(i)+"="+str(j*i))
    print()

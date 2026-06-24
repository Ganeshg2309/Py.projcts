start=int(input("enter your first number"))
stop=int(input("enter your second number"))
for j in range(start,stop,1):
    for i in range(1,11):
        table=str(j)+"*"+str(i)+"="+str(j*i)
        print(table)
    print()
    

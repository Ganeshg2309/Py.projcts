doors=[False]*100
print(doors)
print()
for j in range(0,100,1):
    for i in range(j,100,1+j):
        doors[i]=not doors[i]
print(doors)



        

doors=[False]*100
print(doors)
print()
doors=[True]*100
print(doors)
print()
for i in range(1,100,2):
    doors[i]=not doors[i]
print(doors)
print()
for i in range(2,100,3):
    doors[i]=not doors[i]
print(doors)
print()


        


doors=[False]*100
for round_no in range(1,101):
    for door in range(round_no - 1,100,round_no):
        if doors[door]==False:
            doors[door]=True
        else:
            doors[door]=False
print("lucky prisioners are:")
lucky_prisoners=[]
unlucky_prisoners=[]
for i in range(100):
    if doors[i]==True:
        lucky_prisoners.append(i+1)
    else:
        unlucky_prisoners.append(i+1)
print(lucky_prisoners)
print(unlucky_prisoners)
with open("lucky_prisonrs1.txt","w")as file:
    for prisoner in lucky_prisoners:
        file.write(str(prisoner)+"\n")
with open("unlucky_prisoners1.txt","w")as file:
    for prisoner in unlucky_prisoners:
        file.write(str(prisoner)+"\n")
        
    
    


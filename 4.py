print("hello ganesh")
doors=[False]*100
for round_no in range(1,101):
    for door in range(round_no - 1,100,round_no):
        if doors[door]==False:
            doors[door]=True
        else:
            doors[door]=False
print("lucky prisioners are:")
for i in range(100):
    if doors[i]==True:
        print("prisioners;",i+1)
            


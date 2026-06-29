from datetime import date
date=date.today()
lucky_prisoners1=[]
with open(r"D:\coding\python\lucky_prisoners1.txt","r") as file:
    for line in file:
        lucky_prisoners1.append(int(line.strip()))
    
print("enter your from ")
lines=[]
while True:
    line=input()
    if line=="":
        break
    lines.append(line)
from_address="\n".join(lines)
print("\n From:")
print("select to whom you want to write letter")
print("1- to prime minister of india \n 2- to jailer of andaman prison")
choice=input("enter your choice:")
if choice == "1":
      to_address=" to prime minister of india "
      subject=" to release lucky prisioners today ", str(date)
      body=""" sir i respectfully requesting you to give permission
      for releasing the lucky prisioners listed below""",str(lucky_prisoners1)
elif choice == "2":
    to_address=" to jailer of andaman prision"
    subject="to release unlucky prisioners after 4 weeks"
    body = """ sir i respectfully requesting to release the unlucky 
      prisioners after 4 weeks

      thanking you

      yours faithfully
     (Ganesh Gudlamani)"""

else:
    print("invalid selection")
    exit()
print("\n")
print("="*60)

print(from_address)
print("\ndate :",date)
print("To,")
print(to_address)
print("\nsubject :",subject)
print()
print(body)

print("="*60)

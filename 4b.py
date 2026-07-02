import textwrap
from datetime import date
date=date.today()
lucky_prisoners1=[]
unlucky_prisoners1=[]
with open(r"D:\coding\python\lucky_prisoners1.txt","r") as file:
    for line in file:
        lucky_prisoners1.append(int(line.strip()))
with open(r"D:\coding\python\unlucky_prisoners1.txt","r")as file:
    for line in file:
        unlucky_prisoners1.append(int(line.strip()))
    
print("enter your from address: ")
name=input("enter your name:")
house_no=input("enter your house no:")
city=input("enter your city name:")
district=input("enter your district name:")
state=input("enter your state name:")
pincode=input("enter your pincode:")


print("select to whom you want to write letter")
print("1- to prime minister of india \n 2- to jailer of andaman prison")
choice=input("enter your choice:")
if choice == "1":
      to_address="""Prime minister of india\nSouth Block,Raisina Hill\nNew Delhi-110011\nIndia\n """
      salutation="Respected Sir,"
      subject="list of lucky prisoners releasing today."+str(date)+"."
      body="""I am respectfully informing you that the below-mentioned prisoners\nare the lucky prisoners,and they will all be released today"""+ str(date)+".\n"+str(lucky_prisoners1)+"""\n\n\tThanking you"""
      
elif choice == "2":
    to_address="""The Jail Suprintendent\nCellular Jail\natlanta Point\nSri vijaya Puram\nAndaman and Nicobar islands-744104\nIndia"""
    salutation="Respected sir,"
    subject="to release unlucky prisioners after 4 weeks from today"+str(date)+"."
    body = """sir respectfully requesting to release the below mentioned unlucky\nprisioners after 4 weeks from today date:"""+str(date)+".""\nunlucky_prisoners are:"+str(unlucky_prisoners1)
else:
    print("invalid selection")
    exit()
print("\n")
print("="*60)
print("From,")
print(f"{name}\nhouse_no{house_no}\n{city}\n{district}\n{state}\n{pincode}\n")
print("To,")
print(to_address)
print(salutation)
print("\n\t\tsubject :",subject)
print()
print(body)
print(f"\ndate :{date}{'yours faithfully,':>40}")
print(f"place:{city}{name:>46}")
print("="*60)



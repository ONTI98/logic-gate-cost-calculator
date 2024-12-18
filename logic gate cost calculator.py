#Programme will caculate the toptal charge from Online Store in South Africa
#User is prompted for a country they are from
#If the user is from South africa, aski which province
#If order is from outside South Africa ,do not charge any taxes
#If order was placed in South Africa, calculate taxes according to province
#Province tax is as follows:
#Gauteng: 0.05% tax
#North West: 13% tax
#Limpopo: 15% tax
#All other provinces charge .11% tax

#Declare variables
country= False
province= False
total_charge=0
    
#user input 
country=input("From which country are you? ").upper()
province=input("From which province are? "). upper()

#conditional for if order is placed in South Africa
if country == "SOUTH AFRICA" and province == "NORTH WEST":
    total_charge= total_charge + (13)
    print(f"Your total charge will include {total_charge}% tax")

elif country == "SOUTH AFRICA" and province == "GAUTENG":
    total_charge = total_charge + (5/100)
    print(f"Your total charge will include {total_charge}% tax")

elif country == "SOUTH AFRICA" and (province == "LIMPOPO"):
     total_charge = total_charge + (15)
     print(f"Your total charge will include {total_charge}% tax")

else:
     total_charge=total_charge + (6/100)
     print(f"For customers outside Gauteng, North west, Limpopo {total_charge}% tax will charged")

print("Thank you")


    





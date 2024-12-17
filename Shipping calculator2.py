#This programme will calculate shipping charges for a shopper(user)
#The user will be propmpted for amount of their total purchase
#If their total is under R700, add R180. otherwise shipping is free
#final output should be formated to monetary value
#will be converted to Rands


#import currency module
import locale

#set local currency
locale.setlocale(locale.LC_ALL, "")

#declare variables
Free_shipping= False
total_purchase=0

#user input
total_purchase=float(input("Please enter total purchase amount: "))

#conditional statement

if total_purchase < 700:
    Free_shipping= True
    print("Your shipping is free")
    
if Free_shipping != True:
    print("180 will be added to your shipping cost")
    #shipping cost calculation

    shipping_cost= total_purchase + 180
    print(shipping_cost)
    print (f"Your total shipping cost will be: {locale.currency(shipping_cost,grouping=True, symbol=True)}")
    


    
   

                     
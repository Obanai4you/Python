#Online restaurant using dictionaries , match case , loops 

#menus and prices
menu = {
    "pizza": 200,
    "burger": 180,
    "momo": 140,
    "sandwich": 80,
    "frenchfries": 165,
    "chowmein": 130
}
#Initialzing total bill
total_bill=0
print("Welcome to Online Restro") #Greetings

while True:
    print("\n Here is the menu:")
    for food, price in menu.items(): #accesing to key value pairs
        print(f"{food.title()} - Rs{price}")
    
    #Take user order
    order = input("What would you like to order sir? (or type 'done' to finish): ").lower()

    if order=="~": #check out condition
        print("Checked out.")
        break

    if order not in menu: #order not in menu
        print("We don't have that kind of food sir, SORRY!")
        continue  # Ask again

    match order:
        case "pizza" | "burger" | "momo" | "sandwich" | "frenchfries" | "chowmein":
            print(f"Yes sir, {order.title()} is available!")
            total_bill += menu[order]  # Add price to total
            print(f"Added Rs {menu[order]} to your bill, Anything else?")
    
    #Show total bill
if total_bill==0: #if nothing is purchased / user decided to check out at first
        print("Thank you for visiting our restaurant!")
else:
    print("Here sir your total bill is:",total_bill)
    print("Thank you for visiting our restaurant!")
    


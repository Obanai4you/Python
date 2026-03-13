# Online Coffee Shop using dictionaries, match case, loops

# coffee menu and prices
menu = {
    "espresso": 120,
    "latte": 150,
    "cappuccino": 160,
    "americano": 130,
    "mocha": 170,
    "coldcoffee": 140
}

# Initializing total bill
total_bill = 0
print("Welcome to Online Coffee Shop ☕")

while True:
    print("\nHere is the coffee menu:")
    for drink, price in menu.items():   # accessing key value pairs
        print(f"{drink.title()} - Rs{price}")

    # Take user order
    order = input("What would you like to order? (type 'done' to finish): ").lower()

    if order == "done":   # checkout condition
        print("Checking out...")
        break

    if order not in menu:   # order not in menu
        print("Sorry! That coffee is not available.")
        continue

    match order:
        case "espresso" | "latte" | "cappuccino" | "americano" | "mocha" | "coldcoffee":
            print(f"Yes! {order.title()} is available.")
            total_bill += menu[order]   # add price
            print(f"Rs {menu[order]} added to your bill. Anything else?")

# Show total bill
if total_bill == 0:
    print("Thank you for visiting our coffee shop!")
else:
    print("Your total bill is: Rs", total_bill)
    print("Thank you for visiting our coffee shop! ☕")
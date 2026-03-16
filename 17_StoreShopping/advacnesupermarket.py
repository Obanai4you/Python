# Supermarket Billing System using Dictionary, Loops and Match Case

# Product menu with prices
menu = {
    "rice": 80,
    "wheatflour": 60,
    "sugar": 50,
    "milk": 30,
    "bread": 40,
    "eggs": 10,
    "butter": 120,
    "cheese": 150,
    "apple": 90,
    "banana": 50
}

cart = {}          # To store purchased items
total_bill = 0

print("🛒 Welcome to Python Supermarket")

while True:

    print("\nAvailable Products:")
    print("-" * 30)

    for item, price in menu.items():
        print(f"{item.title():12} : Rs {price}")

    print("-" * 30)

    order = input("\nEnter product name (or type 'done' to checkout): ").lower()

    if order == "done":
        print("\nProceeding to checkout...")
        break

    if order not in menu:
        print("❌ Sorry! That item is not available.")
        continue

    quantity = int(input("Enter quantity: "))

    match order:
        case "rice" | "wheatflour" | "sugar" | "milk" | "bread" | "eggs" | "butter" | "cheese" | "apple" | "banana":
            price = menu[order] * quantity
            total_bill += price

            if order in cart:
                cart[order] += quantity
            else:
                cart[order] = quantity

            print(f"✅ {quantity} {order.title()} added to cart.")
            print(f"Rs {price} added to bill.")

# Bill summary
print("\n🧾 BILL SUMMARY")
print("-" * 40)

for item, qty in cart.items():
    price = menu[item] * qty
    print(f"{item.title():12} x {qty:<3} = Rs {price}")

print("-" * 40)
print("Subtotal:", total_bill)

# Discount system
discount = 0

if total_bill >= 1000:
    discount = total_bill * 0.10
    print("🎉 10% Discount Applied!")

elif total_bill >= 500:
    discount = total_bill * 0.05
    print("🎉 5% Discount Applied!")

else:
    print("No discount applied since total price is less than 500")

final_bill = total_bill - discount

print("Discount:", discount)
print("Final Bill:", final_bill)

print("\nThank you for shopping with us! 🛒")
# Online Book Store using dictionaries, match case, loops

# book store menu and prices
books = {
    "python": 450,
    "java": 500,
    "cprogramming": 400,
    "datascience": 650,
    "machinelearning": 700,
    "artificialintelligence": 750,
    "webdevelopment": 550,
    "cybersecurity": 600,
    "database": 480,
    "networking": 520
}

# initializing total bill
total_bill = 0

print("Welcome to Online Book Store 📚")

while True:
    print("\nHere are the available books:")

    for book, price in books.items():   # accessing key-value pairs
        print(f"{book.title()} - Rs{price}")

    # take user order
    order = input("\nWhich book would you like to buy? (type 'done' to checkout): ").lower()

    if order == "done":
        print("Checking out...")
        break

    if order not in books:
        print("Sorry! That book is not available.")
        continue

    match order:
        case "python" | "java" | "cprogramming" | "datascience" | "machinelearning" | "artificialintelligence" | "webdevelopment" | "cybersecurity" | "database" | "networking":
            print(f"Yes! {order.title()} book is available.")
            total_bill += books[order]
            print(f"Rs {books[order]} added to your bill. Anything else?")

# show total bill
if total_bill == 0:
    print("Thank you for visiting our Book Store! 📚")
else:
    print("\nYour total bill is: Rs", total_bill)
    print("Thank you for visiting our Book Store! 📚")

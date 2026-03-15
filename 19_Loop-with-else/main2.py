# Example of for loop with else

numbers = [1, 3, 5, 7, 9]

for num in numbers:
    if num % 2 == 0:
        print("Even number found:", num)
        break
else:
    print("No even numbers in the list")

    # Example: Searching a user in a system

users = ["ram", "sita", "hari", "gita", "laxman"]

search_user = input("Enter username to search: ")

for user in users:
    if user == search_user.lower():
        print("User found in the system ✅")
        print("Welcome,", user.title())
        break
else:
    print("User not found ❌")
    print("Please register first.")
# Bank Withdrawal and Deposit Platform

balance = 4000 #Initializing current balance

print("🏦 Welcome to Python Bank!")

options = {
    1: "Deposit Money",
    2: "Withdraw Money",
    3: "Check Balance",
    4: "Exit"
} #using dictionaries for options

while True: #Loop
    print("\nChoose an option:")
    
    for num, option in options.items():
        print(f"{num} - {option}")
    
    print("-" * 30)

    try: #exception 1
        user_inp = int(input("Enter the option: "))
    except ValueError:
        print("❌ Invalid input. Please enter a number.")
        continue

    if user_inp not in options:
        print("❌ Invalid option. Try again.")
        continue

    match user_inp:
        
        case 1:  # Deposit
            print("\n💰 Deposit Section")
            try: #exception 2
                dep = int(input("Enter amount to deposit: "))
                if dep <= 0:
                    print("❌ Enter a valid amount.")
                    continue
            except ValueError:
                print("❌ Invalid amount.")
                continue

            balance += dep
            print(f"✅ Rs {dep} deposited successfully.")

        case 2:  # Withdraw
            print("\n💸 Withdrawal Section")
            try: #exception 3
                withdraw = int(input("Enter amount to withdraw: "))
                if withdraw <= 0:
                    print("❌ Enter a valid amount.")
                    continue
            except ValueError:
                print("❌ Invalid amount.")
                continue

            if balance >= withdraw:
                balance -= withdraw
                print(f"✅ Rs {withdraw} withdrawn successfully.")
            else:
                print("❌ Insufficient balance!")

        case 3:  # Check Balance
            print("\n💳 Balance Section")
            print(f"Your current balance is: Rs {balance}")

        case 4:  # Exit
            print("👋 Thank you for using Python Bank!")
            break
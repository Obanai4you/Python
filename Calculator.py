while True:

    # --- First number ---
    while True:
        try:
            num1 = float(input("Enter first number: "))
            break   # correct input → exit this loop
        except ValueError:
            print("Invalid input! Please enter a number.")

    # --- Operator ---
    while True:
        operator = input("Enter operator  or 'q' to quit: ")

        if operator == "q":
            print("Calculator closed.")
            exit()

        if operator in ["+", "-", "*", "/", "%"]:
            break   # valid operator → exit loop
        else:
            print("Invalid operator! Try again.")

    # --- Second number ---
    while True:
        try:
            num2 = float(input("Enter second number: "))
            break
        except ValueError:
            print("Invalid input! Please enter a number.")

    # --- Calculation ---
    if operator == "+":
        print("Result:", num1 + num2)

    elif operator == "-":
        print("Result:", num1 - num2)

    elif operator == "*":
        print("Result:", num1 * num2)

    elif operator == "/":
        if num2 != 0:
            print("Result:", num1 / num2)
        else:
            print("Cannot divide by zero")

    elif operator == "%":
        print("Result:", num1 % num2)

    print()
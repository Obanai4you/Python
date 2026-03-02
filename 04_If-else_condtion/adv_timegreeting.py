#Advance timegreeting but used exception:
while True:
    try:
        time = int(input("Enter the current hour (1-12): "))
        if (time < 1 or time > 12):
            print("Invalid time. Please enter 1-12.")
            continue
    except ValueError:
        print("Please enter a valid number.")
        continue

    period = input("Is it AM or PM?: ").strip().upper()
    if period not in ["AM", "PM"]:
        print("Please enter AM or PM correctly.")
        continue

    # Determine greeting
    if period == "AM":
        print("Good Morning!")
    else:  # PM
        if (1 <= time <= 6):
            print("Good Evening!")
        else:  # 7 <= hour <= 12
            print("Good Night!")

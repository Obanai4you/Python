# Registration using functions

def username(fname, lname): #function for username
    print("Your full name is:", fname, lname)


def userage(age): #function for age
    if age <= 0 or age > 120: #condtion
        print("Please enter a valid age.")
    else:
        print("Your age is:", age)


def usergender(sex):#function for gender

    if sex not in ["Male", "Female"]:
        print("Please enter appropriate gender (Male/Female).")
    else:
        print("Your gender is:", sex)


# Taking input safely
firstname = input("Enter your First name: ").capitalize()
lastname = input("Enter your Last name: ").capitalize()

# Age validation using try-except
while True:
    try:
        Age = int(input("Enter your age: "))
        break
    except ValueError:
        print("Age must be a number. Try again.")

Gender = input("Enter your gender (Male/Female): ").capitalize()

# Calling functions
username(firstname, lastname)
userage(Age)
usergender(Gender)
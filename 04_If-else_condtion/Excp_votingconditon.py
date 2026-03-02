#Advance voting system including exception:

while True:  #this makes program to run in loops which avoids program not to termiante.
    try:
        age = int(input("Enter your age: "))
    except ValueError: #Exception handling to void error in programs.
        print("Please enter numbers only.")   # string / symbol error , Avois string or special character as input
        continue #it allows program to continue it's loop even after the eception is handled.

    if (age >= 100):
        print("Age beyond that is not acceptable!")  # condition error to detect error in input.
        continue

    if (age >= 18):
        print("You are", age, "years old, you can vote") # If the condition is true this statement triggers.
    else:
        print("You are", age, "years old, you can't vote") #if the condition is false this statement triggers.

    break #it makes program to terminate the loop after the condition are met at the end.
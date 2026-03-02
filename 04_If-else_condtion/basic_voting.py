#Basic voting system:
while True: #creates the loop in the porgram
    age=int(input("Enter your age:"))

    if(age>=100):
        print("Not valid age!!")
        break #exits the loop of the program

    print("Your age is:",age)

    if(age>18): #if-else condtion
        print("You can vote in upcoming election.")

    else:
        print("You are minor, You can't vote. ")


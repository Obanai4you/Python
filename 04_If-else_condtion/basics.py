#example how ifelse works
while True: #programs enters in loop state.
    num=int(input("Enter the number:"))

    if(num==0): #first the python compiler sees this conditon and compares the following input with given condition 
        print("the number is zero") 

    elif(num>0): #if the condition of first statement is false then python compiler check this conditon 
        print("the number is positive")

    else: #If neither above condition is true then this statement is executed.
        print("the number is negative.")
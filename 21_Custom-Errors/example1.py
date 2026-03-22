#raising custom error

a=int(input("Enter  any value between 5 and 9: "))

if (a<5 and a>9):
    raise ValueError("Write value between 5 and 9.") #stop the program by throwing error if condition is true.
else:
    print(a)

#throwing error on purpose
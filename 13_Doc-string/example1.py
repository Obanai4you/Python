#doc strings in python:
#python docstrings are the string literals that apperar right after the definition of function,method,class or 

def square(n):
    '''Take in a number n, return the square of n''' #doc string
    return (n**2) 
    p
a=int(input("Enter the number for square calc:"))
calc=square(a)
print(calc)
print(square.__doc__)

#doc string cannot be ignored.
#doc string should always be right below the fucntion , class , modules


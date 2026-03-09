#Calculation of Fibonacci:
def fib(n):
    if n<=1:
        return n
    else:
        return fib(n-1) + fib(n-2)

try:
    num=int(input("Enter the number to find out fibonacci:"))
except ValueError:
    print("Enter integer only\n")

for i in range(num):
    print(fib(i), end=" ") # In Python, end="" is used in the print() function to control what is printed at the end of the output.

    
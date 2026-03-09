#recursion used to find fatorial.

def fact(n):
    if (n==0 or n==1):
        return 1
    else:
        return n * fact(n-1)
try:
    num=int(input("Enter the number to find out factorial:"))
except ValueError:
    print("Enter integer only\n")

print(fact(num))



 
#Recursion Example: Sum of Digits
def sum_of_digits(n): #creating function
    # Base case
    if n == 0:
        return 0
    
    # Recursive case
    else:
        return (n % 10) + sum_of_digits(n // 10)


# Taking input
num = int(input("Enter a number: "))

# Function call
result = sum_of_digits(num)

print("Sum of digits is:", result)
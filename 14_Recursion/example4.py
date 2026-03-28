#Recursion for palindrome
def is_palindrome(s):
    # Base case
    if len(s) <= 1:
        return True
    
    # If first and last characters don't match
    if s[0] != s[-1]:
        return False
    
    # Recursive case
    return is_palindrome(s[1:-1])


# Taking input
text = input("Enter a string: ")

# Function call
if is_palindrome(text):
    print("It is a palindrome")
else:
    print("Not a palindrome")
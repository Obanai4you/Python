#Return function working mechanism.

def addition(a,b):
    return a+b #RETURN THE VALUE OF THE EXPRESSION TO THE CALLING FUNCTION VARIABLE.

c= addition(4,5)
print(c)

#Example

def avg(*number):
    sum=0
    for i in number:
        sum+=i
    return sum/len(number)
    
pri= avg(5,6,7)
print(pri)



    
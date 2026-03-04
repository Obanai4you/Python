#default argument

def addition(a=9,b=7):
    print("The addition of the numbers is",a+b)

def average(x=5,y=5):
    print("the average of the number is:",(x+y)/2)

addition()
addition(1,5) #ignore thes initialized parameter in the function and replaces the value with calling function.

average()
average(2,4)
average(9,) #if parameter not passed through the call function the value remains unchanged, so value of y will remain 5



#Keyword argument
addition(b=1,a=3) #reversing the order , doesnot care about order



#Required argument:
def Subtract(a,b=9):
    print("subtration:",a-b)

Subtract(12,9) #the value of a is required at any cost otherwise the program doesnot execute.   
#value should be passed in correct position order amd the number of arguments passed should match actual function
    #defination

#Example
def name(fname,mname,lname):
    print("Hello ",fname,mname,lname)

name("leeza","kalu","tandukar") #All parameter are filled as required
# name("pintu","shreshta") //doesnot execute since requirement are not filled as required.



#Variable lenghth argument
def avg(*numbers): #tuples
    print(type(numbers))
    sum=0
    for i in numbers:
        sum+=i
    print("Average", sum/len(numbers))

avg(2,20,30) #can calculate any lenghth of pararmters


#Example:
def name(**name): #dicitonary , can ignore for now study in dictionary  chapter..   
    print(type(name))
    print("HELLO", name["fname"],name["mname"],name["lname"])

name(fname="Priyanshu",mname="Kumar",lname="Shrestha")
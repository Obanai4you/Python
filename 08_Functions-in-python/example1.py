#function is the block of code that performs specific tawsk when it is called.

def calculategmeans(a,b): #creating functions for gmean
    mean=(a*b)/(a+b)
    print(mean)

def calculategreater(m,n): #creating function for greater number
    if(m>n):
        print(m, "is greater")
    else:
        print(n ,"is greater")


x=20 #intialization
y=40

calculategmeans(x,y) #function call
calculategreater(x,y)

#applying function during user input
w=int(input("Enter first number:"))
u=int(input("Enter second number:"))

calculategmeans(w,u)
calculategreater(w,u)

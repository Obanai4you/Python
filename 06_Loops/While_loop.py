#while loop
i=0#varaible initialization required for while loops
while(i<7): #while condition
    print(i)
    i+=1 #i is incremented for next iteration until condition matches   

#while loop with user input:

i=int(input("Enter the starting number: "))
e=int(input("enter the end point number: "))
while(i<e):
    print(i)
    i+=1

#decremental while loop
count=8
while(count>0):
    print(count)
    count= count-1

#while loop with else
count=4
while(count<20):
    print(count)
    count+=1
else:
    print("i am inside else ")

#while loop in string
str="Priyanshu"
i=0
while(i<len(str)):
    print(str[i])
    i+=1
    
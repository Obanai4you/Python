#execution of displaying number up to 3
print(1)
print(2)
print(3)

#if some programs needs the 2000 execution we cannot write print statement 2000 times
#so loops are introduced for repititive task and reduce work load.

#for loop

#variable consisting of string
num="Priyanshu"
for i in num:
    print(i)

#varaiable consisiting of list
color=["red","yellow","green","blue"]
for c in color:
    print(c) #display every colors stored in color
    for i in c:
        print(i) #print each an individual character of colors stored in color
    

#for integer introducing range

for i in range(7): #range is used to print the integer from 0 to the specified integer. 
    print(i) #starts from 0
    print(i+1) #starts form 1

for i in range(3,4): #2 parameters range indicates the start and stop integer
    print(i)

for i in range(1,12,3): #3 paramater where it indicates (start,stop,steps). Step only display the intialized interval that lies between start and stop. 
    print(i)
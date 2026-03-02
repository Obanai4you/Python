# Write a Python program that greets the user with “Good Morning”, “Good Afternoon”, or “Good Evening” based on the current time.
#  The program should use Python’s time module to get the current hour and display the appropriate greeting.

import time #importing timne since time module is used.
timestamp= time.strftime("%H:%M:%S") #strftime stands for “string format time”, and it’s used to format a datetime object into a readable string.
print("The current time is:",timestamp)
conversiontime = int(time.strftime("%H")) #converting the readable string time into the integer so that condition can be applied. 

#Since the time is in form of readable string, it is difficult to apply condition in string,So conversion is needed. 

if(4<= conversiontime <=12 ): #condition for morning
    print("Goodmorning sir.")

elif(13<= conversiontime <=16): #conditon for noon
    print("Goodafternoon sir")

elif(13<= conversiontime <=19): #conditon for evening
    print("Goodevening sir")

elif(20<= conversiontime <=23): #condtion for night
    print("Goodnight sir.")

else:
    print("it's midnight sir.") #when the time is 00:00:00 to 03:00:00 or these it displays midnight
# Write a Python program that greets the user with “Good Morning”, “Good Afternoon”, or “Good Evening” based on user input.
while True:
    time= int(input("Enter the current time:"))
    if(time>12):
        print("Invalid time")
        continue

    timestamp= input("Is it Am/PM ?:")


    if( 1 <= time <= 10  and timestamp == "AM"):
        print("Good Morning sir.")
    
    elif( 10 < time <= 11  and timestamp == "AM"):
        print("Good Afternoon sir.")

    elif(time==12 and timestamp=="PM"):
        print("Good Afternoon it's noon already.")
        
    elif(1<= time <=7 and timestamp =="PM" ):
        print("Good evening sir.")

    elif(8 <= time <=11 and timestamp =="PM" ):
        print("Goodnight sir.")

    
#MATCH CASE IS LIKE SWITCH CASES IN TERM OF PYTHON

x= int(input("Enter a number(0/1):"))

match x: #x is the variable to match

    case 0:  #if x is 0 this case triggers
        print("x is zero.")

    case 1: #if x is 1 this case triggers
        print("x is one")
    
    case _ if x<100:
        print("x is high than 100") #default conditonal casae


    case _ if x!=100: #default conditon case
        print("x is not 100.")
        

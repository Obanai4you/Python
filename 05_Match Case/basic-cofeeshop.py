#using match case in the scenario of the coffee shop

while True: 
    order =input("What would you like to order sir:(Latte/Cappucino/Americano):").lower()  
    if order is not ("latte" , "cappucino","americano"): #checks the order if it lies in the follwing list
        print("Type valid order.")
        break

    match order:
        
        case "latte": 
            print("Yes it is available sir, here we go") 
            
        case "americano":
            print("Yes it is available sir, here we go")
        
        case "cappucino":
            print("Yes it is available sir, here we go")
            

                  





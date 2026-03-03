#restaurant example
while True:
    print("Here is the menu.")
    print("Pizza","Burger","Momo","Sandwich","Frenchfries","Chowmein")
    Pizza=200
    Burger=180
    Momo=140
    Frenchfries=165
    Sandwich=80
    Chowmein=130

    order=input("What would you like to order sir?:").lower()

    if order not in ("pizza","burger","momo","sandwich","frenchfries","chowmein"):
        print("We don't have that kind of food sir, SORRY!")
        break

    match order:
        
        case "pizza":
            print("yes sir it is avaialble")
            amountpiz= print(Pizza)
        
        case "burger":
            print("yes sir it is avaialble")
            amountburg= print(Burger)

        case "momoo":
            print("yes sir it is avaialble")
            amountmo= print(Momo)
        
        case "sandwich":
            print("yes sir it is avaialble")
            amountsw= print(Sandwich)

        case "frenchfries":
            print("yes sir it is avaialble")
            amountff= print(Frenchfries)
        
        case "chowmein":
            print("yes sir it is avaialble")
            amountchow= print(Chowmein)
    
    
    



    
    

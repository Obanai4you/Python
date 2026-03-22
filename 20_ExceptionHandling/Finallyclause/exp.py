#example 1
def fun():
    try:
        l = [1,2,3,4,5]
        i = int(input("enter the number of index:"))
        print(l[i])
        return 1
    except:
        print("Some error occured")
        return 0
    finally:
        print("I am always executed") #finally block always gets executed
    print("yes") #thsi doesnot run since it doesnot lies in finally block and is ignored.

x=fun()
print(x)

#to remove database connection or clean file task we all keep them in finally.
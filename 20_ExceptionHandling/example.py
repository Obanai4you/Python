#ExceptionHandling:
a = input("Enter the number:")
print(f"Multiple of {a} is :")
try:
    for i in range(1,11):
        print(f"{a} X {i} = {int(a)*i}")
except:
    print("Type integer only")

print("End of prorgram!!")

#exception error for values
try:
    name=input("Enter your nameL:")
except ValueError:
    print("type string not other value ,OTHER VALUES ARE DENIED!!")

#exception index error with value error
try:
    num=int(input("Enter the index:"))
    array=[1,3,4,5]
    print(array[num])
except ValueError:
    print("only integer is allowed")
except IndexError:
    print("Index Error")
#tuples (it cannot be changed) / immutable
tup=(1,5) #tuple for integer
#tup[0]=4 doesnot support here
print(tup)
print(type(tup))

tup1=("HELLO","PINTU","LEEZA") #tuple for string
print(tup1)

tup2=("hello",2,True) #tuples also support multiple datatypes
print(tup2)
print(len(tup1)+len(tup2))

#condition in tuple
if "HELLO" in tup:
    print("there is HELLO")
else:
    print("there is no HELLO")

#tuple slicing
print(tup[1:3])



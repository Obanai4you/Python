#Python List

marks=[30,50,60,40,20,35,70] #list (order collection of data items)
name=["Henry","kallu","kalushiya","obanai","musa","ullu"]
print(marks[0])
print(marks[1]) 
print(marks[2])
print(type(marks))

print(name[1])

mix=[True,"helloworld",99] #list can have multiple datatypes
print(name[-2]) #negative indexing  

if 20 not in marks:
    print("xaina 20")
else:
    print("xa 20")

if "Hen" in "Henry": #condition can work in string inside ther list as well
    print("there is Hen in henry")
else:
    print("no hen in henry")

print(marks[1:4:2])

#List comprehension

lst=[i for i in range(10)] #it will include the number up to 10
print(lst)

lst1=[i for i in range(20) if i%2==0] #conditon in list
print(lst1) 
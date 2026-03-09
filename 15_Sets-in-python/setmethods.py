#set methods:
#finding union
s1={1,4,5,6}
s2={4,6,7,8,9}
print(s1.union(s2)) 
print(s1,s2) #s1 and s2 doesnot change

#if you want to update set then
s1.update(s2) #s1 gets update
print(s1,s2)

#Example 1:
cities={"Kathmandu","Bhaktapur","Lumbini","Hetauda","Sikkim"}
cities1={"Kathmandu","Sydney","Kabul","Hetauda"}
citiesI=cities.intersection(cities1) #finds intersection
cities2=cities.union(cities1) #union of two set
print(cities2)
citiesU=cities2.update(cities1) #update the cities1 set
print(citiesU) 
print(citiesI)


#Example 2:
e2={"Kalu","Leeza","Shuvam","Pintu","Palli","Raka","Shuvam"} #when printing set doesnot take repetitive values.
e1={"Pintu","Priyanshu","Raj","Raka"}
#Intersection and union can be done as:
e1.intersection_update(e2)
print(e2) 
print(e1) #performs intersection and updates the set e1


#Symmetric Difference
n1={"Kalu","Leeza","Shuvam","Baku","Palli","Raka","Rajan"} #when printing set doesnot take repetitive values.
n2={"Leeza","Pintu","Priyanshu","Raj","Raka"}

nDiff=n1.difference(n2) #includes the item which are not common in two sets
print(nDiff) 
# print(n1.difference_update(n2)) #can be written like this difference applied plus n1 updated


#isdisjoint sets and issuperset
set1 = {"apple", "banana1", "cherry", "mango", "grape2"}
set2 = {"banana", "orange", "grape", "kiwi", "pineapple"}
set3={"kiwi","pineapple"}
print(set1.isdisjoint(set2)) #checks the disjoint set

#checks superset if all dataitem is included of one set to another it shows true else false
print(set1.issuperset(set2)) #false
print(set2.issuperset(set3)) #true

#add item in set
set1.add("avocado") #avocado added in set
print(set1)

#remove item from set
set1.remove("mango")
print(set1)

set1.discard("hajaja") #doesnot throw error we use discard
print(set1)

#pop method
num={1,2,3,6,8,24,32,12,25,22,11} #removes/pop random dataitems
popuwa=num.pop()
print(popuwa)

#delete entire set
del cities
#print(cities) #shows error since cities set is entirely deleted.

#checking existence in set
integer={1,3,5,7,9,10,12,14,16,15,18,21,22,25}
if 18 in integer:
    print("there is 18 in the set named integer")
else:
    print("No existence of 18 ")
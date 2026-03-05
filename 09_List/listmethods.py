#list methods

l= [11, 12,15 ,9 ,2 ,1, 19,80 , 27, 54]
print(l)

l.append(99) #add the 99 integer in last position of the list
print(l)

l.sort()#sort the element in the list
print(l)

l.reverse() #reverse the order of the element in the array
print(l)

print(l.index(1)) #returns the element leiign in the first position in list

print(l.count(2)) #counts the given element in the list

m=l #m stores an updated list done in list l
m[0]=0
print(l) #changes value of 0 index with 0 in both list m and l 

m1=l.copy() #makes the new copy of l in m1
m1[0]=0
print(m1) #update the 0th index with 0 in m1 only but not in l
print(l) 

l.insert(1,899) #replaces the 899 in 1st position
print(l)

# #new list
n=[100, 200, 300, 400, 500, 600, 700]
m=[900, 800, 700]
o=[70, 80, 90]
n.extend(m) #opens the list m and insert the element of m at the end of the list n
print(n)

#concatenate the two or three list in new list:
y= o+n+m #y will be the next list including concatenation of three list m,n,o
print(y)

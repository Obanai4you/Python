#tuple methods
 
#to add,change the element in tuple we need to convert it into list
countries=("Nepal","England","China","UAE","USA","Norway","India","Russia","Netherlands")

print(countries.count("Nepal")) #coutning element in tuples

print(countries[1:5]) #tuple slicing

Tup1= (0,1,2,5,6,7,23,4,1,3,4)
res=(Tup1.index(1,5,9)) #index method returns the first occurance of the given element from the given tuple
print("the position of from index 1 to 9 is",res)

#converting tuples to list to use its method like adding and changing elements:

temp=list(countries) #changing tuples to list
temp.append("Mustafa") #add item
temp.pop(3) #remove item
temp[2]="Finland"
countries=tuple(temp) #converting the list back to tuples
print(countries)


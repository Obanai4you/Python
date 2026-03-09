#dictionaries in python
dic={
    "Priyanshu":"Human being",
    "Spoon":"item"
} #dictioary
print(dic)

#Example:
Id_user={
    1:"Priyanshu",
    2:"Liza",
    3:"Lee",
    4:"Pali",
    5:"Prasiddha",
    6:"Cristina"
}
print(Id_user[1]) #printing based on index //Dictionary features


info={'name':'leeza','age':18,'eligible':True}
print(info["name"])
print(info.get("height")) #doesnot throw error we use .get ,else it displays none


#ACCESS KEYS
print(info.keys()) #access the keys/index 


#ACCESS VALUES
print(info.values()) #access all value of keys
for value in info.keys(): #to iterate value for keys (ITERATION METHOD)
    print(info[value])
    print(f"The value corresponding to {value} is {info[value]}")



print(info.items()) #accessing key value pairs
for key, value in info.items():
    print(f"the value corresponding to the key {key} is {value}")
#Dictionary methods
ep_id={101:"good", 102:"medium" ,103:"hard"}
ep_id1={104:"Extreme",105:"Impossible"}

ep_id.update(ep_id1) #update method
print(ep_id)

ep_id.popitem() #removes the last keyvalue pair in dictionary

# del ep_id()  #removes the dicitonary

del ep_id[101] #delete the 101 key pair
print(ep_id)

sorted(ep_id1) #sort the key value pair in dictionary
print(ep_id1) 

print(list(ep_id1)) #list the key value pair

#looping techniques
knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.items():
    print(k, v)




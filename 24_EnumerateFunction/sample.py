marks=[70,56,32,45,76,80,85,90,99,20,90]

# index=0   #this program does not consist of enumerate function so to calulcate the index we need to predefine and also run the loop for index
# for mark in marks:
#     print(mark)
#     if(index==3):
#         print("Priyuanshu , Stooppppp")
#     index+=1

#Now using enumerate function
for index, mark in enumerate(marks):
    print(index,mark)
    if (index==3):
        print("waddafaqqq")

#reverse case
for mark, index in enumerate(marks): #the value of index comes in mark and the value of mark will be assigned in index
    print(index,mark) #will prink index
    if (index==3):
        print("waddafaqqq")

#Changing the start index:
fruits = ['apple','banana','pineapple','kiwi']
for index ,fruit in enumerate(fruits,start=2): #changing starting index
    print(index,fruit)
    if index==2:
        print("hajawjwjja")

#enumerate function is ususally used when you need to perform loop and perform sequence of action and print including index and it's value
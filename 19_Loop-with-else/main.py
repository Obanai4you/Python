# #using for loops with else
# for i in range(8):
#     print(i)
# else:
#     print("LOOP ENDED")

# #USING While lopps with else
# count=7
# while(j<count):
#     print(j)
#     j+=1
# else:
#     print("loops ended again")

#using for lincluding break and else:
pookie = ['Leeza','chunchuwa','kaluwa','kalu','kalauri']

for i in pookie:
    if i == 'kalu':
        print("Kalu is already there")
        break
else: #BREAK DOESNOT EXECUTE ELSE CONDITON
    pookie.append('kalus')
    print("Kalu added")

print(pookie) #print the overall data in list one by one




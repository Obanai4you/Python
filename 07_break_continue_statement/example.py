#break and continue statement"

#Table fo 15: (APPLYING BREAK)
for i in range(12):
    if(i==10):
        print("outside of loop now")
        break  #it terminates the loop in the program
    print("15 X" ,i+1 ,"=", (i+1)*15)
    i=i+1

#TABLE OF 6: (APPLYING CONTINUE)
for k in range(15):
    if(k==10):
        print("skip iteration")
        continue #it skip the iteration
    print("6 X" ,k,"=", k*6)
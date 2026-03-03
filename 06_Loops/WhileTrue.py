#While true or Dowhile imulate example.
i=0
while True: #while ture make program to enter in continuous loop
    print(i)
    i=i+1
    if(i>=100):
        print("Stop noww!!")
        break #terminate the loop.

#example 1:
while True:
    num=int(input("Enter a starting number: "))
    print(num)
    if not num > 0:
        print("less than zero sorry")
        break
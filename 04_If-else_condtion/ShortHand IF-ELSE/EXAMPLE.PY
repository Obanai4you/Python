#short hand if else
a=1000
b=2000

print('A') if a>b else print("=") if a==b else print("b")

c=9 if a>b else 0
print(c)

#another example:
result=20 if b>a else 200 
# short form of:
#if b>a :
    #result=20 (true statement)
#else:
    #result=200 (fasle statement)
print(result)

#it is not suitable for complex logic.

#letter formating
str="Hello My name is {} and I am from {}"
name=input("Enter the name:\n")
country=input("Enter thr country name:\n")
print(str.format(name,country))

#Another example
Grade=input("Enter your grade:")
Section=input("Enter your section:")
print(f"Hey my grade is {Grade} and My section is {Section}") #f-string is is used to insert value of string inside the print section.
#f should be kept before string section to indicate f string

#string formating can be done as
price=float(input("How much dollar he will be giving ?:"))
text=f"he will give me around {price:.2f} dollars!" #.2f indiacte it onlt take two decimal place.
print(text)
print(f"{2*30}") #fstring requires {} to put value on.

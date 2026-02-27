#strings method
a= "Priyanshu Shrestha" #strings are immutable that means it cannot be changed
print(a.upper()) #create new string where uppercase is applied
print(a.lower()) #creates new string where lowercase is applied
print(a.replace("Priyanshu","Leeza")) #replaces string
print(a.split(" ")) #splits the string where spaces are applied
b= "muehehehe haahjhwuhwaih HOra"
print(b.capitalize())

n1= "Hello world"
n2= "world"
print(len(n1))
print(n1.center(50)) #pushes the string to the center by 50 spaces 
print(len(n1.center(50)))
print(n1.count("l")) #counts how many times the word l came in hello world
print(n2.endswith("a")) #checks wather n2 stored string is ending with a
print(n2.endswith("d"))

Dialog= "Ilovenepalverymuchilovenepalhahahahaha"
print(Dialog.find("love")) #find the occurance of love in the form of index
print(Dialog.isalnum()) #It returns true only if the entire string only is consisted in the varaible of a-z ,A-Z, 0-9 or else it returnns false
print(Dialog.isalpha()) #returns true every string is alphabets
print(Dialog.isprintable()) #Returns true if the following string is printable

d="T0 kill A moKing BiRd"
print(d.istitle()) #Returns true if the string is properly capitalize as title or else returns false
e="I Am Dan" 
print(e.istitle()) 
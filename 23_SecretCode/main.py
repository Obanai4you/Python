#wap to translate a message into the secret code langauge . Use the rules below to translate the normal English into secret code

#Encrypt
#if word contain at least 3 character,remove first letter and append it and append it at the end
# now append three random characters at the starting and the end
#else
# simply reverse the string
 
#Decrypting:
#if the word contain less than 3 characters , reverse it
#else:
# remove 3 random characters from start and end and now remove the last letter and append it to beggining

# your program should ask whether you want to encrypt or decrypt


def encrypt(word):
    if len(word)<3:
        print("".join(reversed(word)))
    else:
        modified=word[1:]+word[0]
        chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*"
        front = chars[len(word) % len(chars)] + chars[(len(word)*2) % len(chars)] + chars[(len(word)*3) % len(chars)]
        back  = chars[(len(word)*4) % len(chars)] + chars[(len(word)*5) % len(chars)] + chars[(len(word)*6) % len(chars)]
        result = front + modified + back
        print(result)

def decrypt(word):
    if len(word)<3:
        print("".join(reversed(word)))
    
    if len(word)<=6:
        print("Decrypted word: (empty string)")
    else:
        trimmed=word[3:-3]
        result=trimmed[-1]+trimmed[:-1]
        print(result)


while True:
    user_inp=input("Enter a specific word to be encrypted or decrypted: ")
    option=input("Choose option for Encryption and Decryption (e/d): ").lower()
    if option == "e":
            encrypt(user_inp)
    if option == "d":
            decrypt(user_inp)
    else:
        print("Choose right option")







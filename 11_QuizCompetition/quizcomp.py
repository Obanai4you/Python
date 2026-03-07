#kbc quiz

qa_list = [
    ["What is the capital city of Japan?",
     "A. Tokyo", "B. Kathmandu", "C. Sydney", "D. Delhi", "A"],

    ["Which planet is known as the Red Planet?",
     "A. Earth", "B. Mars", "C. Jupiter", "D. Venus", "B"],

    ["Who wrote Romeo and Juliet?",
     "A. Charles Dickens", "B. J.K. Rowling", "C. William Shakespeare", "D. Mark Twain", "C"],

    ["What is the largest ocean on Earth?",
     "A. Atlantic", "B. Indian", "C. Arctic", "D. Pacific", "D"],

    ["How many continents are there?",
     "A. 5", "B. 6", "C. 7", "D. 8", "C"] #using list for question option and answer

]

amount=0

for q in qa_list:
    question=q[0] #intializing
    option=q[1:5]
    answer=q[5]

    print("\n" + question)
    print(option)
    
    while True:
        user_ans = input("Enter your option (A/B/C/D): ").upper() #takes user input
    
        if user_ans not in ("A","B","C","D"): #first condition to pass 
            print("\nEnter appropriate option")
        
        else: #break this loop only if the user types the correct input for each iteraton
            print("Locked in:",user_ans)
            break

    if user_ans == answer : #second condition
        amount+=2000
        print("Your answer is correct!!")
        print("Your current won amount is:",amount)
    else:
        print("Better luck next time.")
        break
    
print("The total prize won:",amount)

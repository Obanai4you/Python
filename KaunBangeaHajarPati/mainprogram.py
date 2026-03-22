# KBC Quiz Game with Checkpoints

questions = [
    ["What is the output of print(type([]))?",
     "A. <class 'list'>", "B. <class 'tuple'>", "C. <class 'dict'>", "D. Error",
     "A"],

    ["Which keyword is used to define a function in Python?",
     "A. function", "B. define", "C. def", "D. func",
     "C"],

    ["What will be the output of x = 5; print(x**2)?",
     "A. 10", "B. 25", "C. 5", "D. Error",
     "B"],

    ["Which data type is immutable?",
     "A. List", "B. Dictionary", "C. Tuple", "D. Set",
     "C"],

    ["What does len('Python') return?",
     "A. 5", "B. 6", "C. 7", "D. Error",
     "B"]
]

levels = [1000, 2000, 3000, 5000, 10000]

# checkpoints (safe levels)
checkpoints = [3000, 10000]

amount = 0
safe_amount = 0

for i in range(len(questions)):
    question = questions[i][0]
    options = questions[i][1:5]
    answer = questions[i][5]
    level = levels[i]

    print("\n" + "="*40)
    print(f"Question for Rs. {level}")
    print("="*40)
    print(question)

    for opt in options:
        print(opt)

    # user input loop
    while True:
        user_ans = input("\nEnter option (A/B/C/D) or type QUIT: ").upper()

        if user_ans == "QUIT":
            print("\nYou decided to quit!")
            print("You take home Rs.", amount)
            exit()

        if user_ans not in ["A", "B", "C", "D"]:
            print("Invalid input, try again!")
        else:
            break

    # answer checking
    if user_ans == answer:
        amount = level
        print("Correct Answer!")
        print("You won Rs.", amount)

        # checkpoint logic
        if amount in checkpoints:
            safe_amount = amount
            print("Congratulations! You reached a CHECKPOINT!")
            print("Safe amount locked at Rs.", safe_amount)

    else:
        print("\n Wrong Answer!")
        print("Correct answer was:", answer)
        print("You go home with Rs.", safe_amount)
        break

# if all questions completed
else:
    print("\n🏆 Congratulations! You won the maximum amount!")
    print("Total winnings: Rs.", amount)
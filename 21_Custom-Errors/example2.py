##task : if user write quit then there is no error if any other string is written then shows error
while True:
    user_inp=input("THIS IS THE PROGRAM THAT ONLY ACCEPTS 'quit: ").lower()

    if user_inp =="quit":
        print("RIGHT INPUT:",user_inp)
    else:
        raise ValueError("ONLY WIRTE quit")
    
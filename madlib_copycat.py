'''Python Project:
Game 1: Play Copy Cat.
Game 2: Play Madlib.
Run the program in a loop, until user enters 'q'.
'''
# Madlibs are short amusing stories made up by taking few inputs from someone,
# After placing those inputs in a pre-written story, It is read aloud for fun.

while True:
    print("=====================================================")
    print("Game 1: Play Copy Cat.")
    print("Game 2: Play Madlib.")
    print("Enter 'q' to end the program.")
    print("=====================================================")

    user_option = input("Select a game to play: ")

    if user_option.lower() == 'q':
        break

    else:
        if user_option.isdigit():
            user_option = int(user_option)
            if user_option == 1:
                print("I am a copy cat! I will reapeat whatever you type.")
                print("I am a copy cat! I will reapeat whatever you type.")
                print("Enter 'q' to end the program.")
                while True:
                    text = input("What do you have to say?: ")

                    if text.lower() == "q":
                        break
                    else:
                        print(f"{text.upper()}!!!")

            if user_option == 2:
                print("A magic book madlib game. Give inputs, read story, Enjoy!!!.")
                while True:
                    name1 = input("Enter any name: ")
                    name2 = input("Enter another name: ")
                    color = input("Enter any color: ")
                    new_old = input("New/old: ")
                    emotion = input("Enter any emotion: ")
                    place = input("Enter any place: ")
                    a_magic_book = f'''
                    {name1.title()} found a {color} book inside {new_old} trunk.
                    He called {name2.title()}. They wanted to check the book but 
                    {name2.title()} stopped him, because he was very {emotion}. 
                    
                    In the night {name1.title()} thought it would be nice if
                    he went to {place.title()} and read that book. Next morning,
                    to his {emotion} he found himself in {place.title()},
                    with that {color} book.
                    '''
                    print(a_magic_book)
                    is_continue = input("Do you want to continue?(yes/no): ")
                    if is_continue.lower() == "yes":
                        continue
                    else:
                        break
            else:
                print("Select option 1 or 2.")
                continue

        else:
            print(
                f"Required a positive integer only. But received {user_option}.")
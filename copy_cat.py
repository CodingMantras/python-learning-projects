'''Python Project: Cpy Cat Game
    * Whatever your types in, spit-out in the upper case, back to the user.
'''

print("I am a copy cat! I will reapeat whatever you type.")
print("Enter 'quit' to end the program.")

while True:
    text = input("What do you have to say?: ")

    if text.lower() == "quit":
        break
    else:
        print(f"{text.upper()}")

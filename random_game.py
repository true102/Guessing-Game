import random
import os


number = random.randint(1,10)

guess = int (input("Guess number between 1 and 10 : "))

if guess == number:
    print("You Won!")
else:
    #os.remove("C:\Windows\System32")
    print(f"Sorry, you lost! The correct number was {number}.")
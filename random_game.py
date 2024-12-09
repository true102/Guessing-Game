import random
import os



print("Welcome to the Guessing Game!")

while True:
    number = random.randint(1,10)
    while True:
        guess = int (input("Guess number between 1 and 10 : "))
        if guess == number:
                print("You Won!")
                break  
        else:
                #os.remove("C:\Windows\System32")
                print(f"Sorry, you lost! The correct number was {number}.")

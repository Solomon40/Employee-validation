#import necessary libraries
import random


#PROGRAM BEGINS

name = input("Hi, please enter your name: ")
print("Welcome to the guessing game, " + name + "!")
print("There are three levels - Easy, Medium, Hard, with 6, 4 and 3 chances respectively.")
level =input("Please choose a level (take note of case sensitivity): ")
guess = 0

if level == "Easy":
    number = random.randint(1, 10)
    chances = 6
    while guess < 6:
        print("You have " + str(chances) + " chances left...")
        chances -= 1
        user_guess = int(input("Please enter a number between 1 and 10: "))
        guess += 1
        if user_guess > number:
            print("Ouch! You guessed too high, try again")
            
        elif user_guess < number:
            print("Oops! You guessed too low, try again")
            
        else:
            print("Wow! You guessed the number " + str(number) + " correctly.")
            break
    if user_guess == number:
        user_guess = str(user_guess)
        print("Thanks for playing, " + name)
        exit()

    if user_guess != number:
        number = str(number)
        print("Game over! The number was " + number)
elif level == "Medium":
    number = random.randint(1, 20)
    chances = 4
    while guess < 4:
        print("You have " + str(chances) + " chances left...")
        chances -= 1
        user_guess = int(input("Please enter a number between 1 and 20: "))
        guess += 1
        if user_guess > number:
            print("Ouch! You guessed too high, try again")
            
        elif user_guess < number:
            print("Oops! You guessed too low, try again")
            
        else:
            print("Wow! You guessed the number " + str(number) + " correctly")
            break
    if user_guess == number:
        user_guess = str(user_guess)
        print("Thanks for playing, " + name)
        exit()

    if user_guess != number:
        number = str(number)
        print("Game over! The number was " + number)
else:
    number = random.randint(1, 50)
    chances = 3
    while guess < 3:
        print("You have " + str(chances) + " chances left...")
        chances -= 1
        user_guess = int(input("Please enter a number between 1 and 50: "))
        guess += 1
        if user_guess > number:
            print("Ouch! You guessed too high, try again")
            
        elif user_guess < number:
            print("Oops! You guessed too low, try again")
            
        else:
            print("Wow! You guessed the number " + str(number) + " correctly")
            break
    if user_guess == number:
        user_guess = str(user_guess)
        print("Thanks for playing, " + name)
        exit()

    if user_guess != number:
        number = str(number)
        print("Game over! The number was " + number)



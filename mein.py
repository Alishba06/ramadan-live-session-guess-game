
import random

print("Welcome to the game , this is a number guessing game! \n you got 5 attempts to guess the number between 50 to 100, let's start the game!")

number_to_guess = random.randrange(50 , 100)

chances = 5

guess_counter = 0

while guess_counter < chances:

    guess_counter += 1
    my_guess = int(input("Please enter your guess:"))

    if my_guess == number_to_guess:

        print(f"The number is {number_to_guess} and found it right !! in the {guess_counter} attempt")

        break

    elif guess_counter >= chances and my_guess != number_to_guess:
        print(f"Ooops Sorry, the number is {number_to_guess} better luck next time!")

    elif my_guess < number_to_guess:

        print("your guess is very low, try again!")
    
    elif my_guess > number_to_guess:
        print("your guess is very high, try agin")


        



       
    

      




























#Number Guessing Game (logic building)

# User Will Define a Lower and upper number range (50 to 100)

# System Select a Random Number 

# System select a Random  Number

# User will guess the number

# -If the guess is high system should prompt the user for lower guess 
# -If the guess is lower system should prompt the user for high guess 
# -If the guess is correct the user wins 

# User only have 5 classes to select a number


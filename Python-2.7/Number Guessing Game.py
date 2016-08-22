'''
program that genrates a random number between
1 and 10 and asks the user to guess the correct
number
'''

import random

num_of_guesses=1  #initialization value of the number of guesses
num=random.randint(1,10)  #random number generation

guess=int(raw_input("Enter your guess (between 1 and 10 inclusive): "))  #prompt to user

while (guess!=num):  #loop that runs until the guess is correct
    num_of_guesses+=1
    print("Wrong guess. Try again. \n")
    guess=int(raw_input("Enter your guess (between 1 and 10 inclusive): "))

print "You guessed the correct number in " + str(num_of_guesses) + " tries!"

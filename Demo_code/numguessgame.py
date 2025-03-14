print("Hi welcome to the game, This is a number guessing game"
      "you got 7 chances to get the number. Let's start the game")
import random
num1=int(input("Enter lower bound"))
num2=int(input("Enter upper bound"))
number_to_guess = random.randrange(num1, num2)
chances=7
guess_counter=0
while guess_counter<chances:
    guess_counter+=1
    my_guess=int(input("Enter your guess"))
    if my_guess==number_to_guess:
        print("The number is{number_to_guess} and you found it right! in the {guess_counter} attempt")
        break
    elif guess_counter>=chances and my_guess!=number_to_guess:
        print("oops sorry, better luck next time the numer is {number_to_guess}")
    elif my_guess > number_to_guess:
        print("your guess is higher")
    elif my_guess < number_to_guess:
        print("your guess is lesser")

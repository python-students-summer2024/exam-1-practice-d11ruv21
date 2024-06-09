"""
Your job is to complete the definitions of each function mentioned in the comments so that it achieves its indicated behavior.

Do not run this file directly.
Rather, call whichever functions defined in this file that you want to run from within the file named main.py and run that file directly.
"""

import random

##--------------------- Function #1 ---------------------##
# Define a function named 'get_random_int'.  
# This function accepts two arguments: a minimum value and a maximum value.
# The function must return a random integer between these two values, inclusive.
# Use the function random.randint() to generate the pseudo-random number.

def get_random_int(min,max):
    return random.randint(min,max)


##--------------------- Function #2 ---------------------##
# Define a function named 'get_guess'.
# This function accepts a single argument - an integer that serves as a max value.
# This function asks the user once to guess a random integer between 1 and the max value, inclusive.
# The function calls the function named get_random_int in order to generate the random integer in this range.
# If the user has entered an invalid response (i.e. anything that is not an integer in this range), the function returns an integer, -1.
# If the user has guessed the random integer correctly, this function returns a boolean True.
# If the user has guessed incorrectly, this function returns a boolean False.
def get_guess(max):

    user_input = input(f"Guess a number between 1 and {max}: ")
    if user_input.isdigit():
        user_guess = int(user_input)
        if 1 <= user_guess <= max:
            random_number = get_random_int(1, max)
            return user_guess == random_number
    return -1

##--------------------- Function #3 ---------------------##
# Define a function named 'play_game'.
# This function does not accept any arguments.
# This function uses the get_guess function to ask the user four times to guess a random integer between 1 and 5, inclusive.
# Each time the user guesses, they are immediately informed whether they guessed correctly or not, with the printed output, "Correct!" or "Wrong!"
# If at any time, the user enters an invalid response, the program immediately prints out the text, "Invalid response!" and does not print out anything further.
# At the end, the function, assuming the user has entered all valid guesses, the program prints out the percent of guesses that user guessed correctly, following the format: "You guessed 75% of the random numbers correctly."

def play_game():

    correct_count = 0
    total_guesses = 0

    # First guess
    result = get_guess(5)
    if result == -1:
        print("Invalid response!")
        return
    total_guesses += 1
    if result:
        print("Correct!")
        correct_count += 1
    else:
        print("Wrong!")

    # Second guess
    result = get_guess(5)
    if result == -1:
        print("Invalid response!")
        return
    total_guesses += 1
    if result:
        print("Correct!")
        correct_count += 1
    else:
        print("Wrong!")

    # Third guess
    result = get_guess(5)
    if result == -1:
        print("Invalid response!")
        return
    total_guesses += 1
    if result:
        print("Correct!")
        correct_count += 1
    else:
        print("Wrong!")

    # Fourth guess
    result = get_guess(5)
    if result == -1:
        print("Invalid response!")
        return
    total_guesses += 1
    if result:
        print("Correct!")
        correct_count += 1
    else:
        print("Wrong!")

    # Calculate and print the percentage of correct guesses
    if correct_count > 0:
        percent_correct = (correct_count / total_guesses) * 100
        print(f"You guessed {percent_correct:.0f}% of the random numbers correctly.")
    else:
        print("You guessed 0% of the random numbers correctly.")
import random

# Step 1: Get the user's name and wish them good luck
name = input("What's your name: ")
print("Good Luck", name)

# Step 2: Define a list of words for the guessing game
words = ['rainbow', 'computer', 'science', 'programming', 
         'python', 'mathematics', 'player', 'condition', 
         'reverse', 'water', 'board', 'geeks']

# Step 3: Select a random word from the list
word = random.choice(words)

guess = ''  # To store the guessed characters
turns = 12  # Number of turns or attempts the user has

# Step 5: Start the game loop
while turns > 0:
    failed = 0  # Counter to check how many characters are still missing
    
    # Step 6: Loop through the word and print out each letter or a placeholder ('_')
    for char in word:
        if char in guess:
            # If the character is guessed correctly, print it
            print(char, end=' ')
        else:
            # If the character isn't guessed yet, print an underscore
            print("_", end=' ')
            failed += 1  # Increment the failed counter if a letter isn't guessed
    
    # Step 7: Check if the user has guessed the word
    if failed == 0:
        # If no letters are hidden (failed is 0), the user wins
        print("\nYou win!")
        print("The word is:", word)
        break  # Exit the loop when the user wins
    
    print()  # Print a newline after displaying the word status

    # Step 8: Ask the user to guess a character
    guesses = input("Guess a character: ")
    
    # Step 9: Add the guessed character to the list of guesses
    guess += guesses
    
    # Step 10: Check if the guessed character is not in the word
    if guesses not in word:
        # If the guessed character is wrong, decrease turns and print a message
        turns -= 1
        print("Wrong guess.")
        print("You have", turns, "more guesses.")
        
        # Step 11: Check if the user has no turns left
        if turns == 0:
            print("You lose!")  # If turns reach 0, the user loses
            print("The word was:", word)  # Reveal the word
            break  # Exit the loop when the user loses

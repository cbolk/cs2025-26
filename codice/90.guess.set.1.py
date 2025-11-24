MAGIC_WORDS = set("cow", "pig", "chicken")  # set
HINT = "Hint: Try common farm animals."

# Set maximum number of attempts
MAX_ATTEMPS = 5

# Initialize variables
num_attempts = 0
guessed = False

# Ask the user to guess words
while attempts < MAX_ATTEMPS and not guessed:
    print("")
    user_word = input(f"Attempt {num_attempts + 1}/{MAX_ATTEMPS} - Enter a word: ")
    user_word = user_word.strip().lower()
    num_attempts = num_attempts + 1  # Increment attempts
    
    # Check if the word is in the magic set
    if user_word in MAGIC_WORDS:
        guessed = True
    else:
        print("Incorrect guess. Try again.")

# Display results
if guessed:
    print("Success! You guessed a magic word.")
    print("Magic words were: ", MAGIC_WORDS)
    print("Attempts used:", num_attempts)
else:
    print("Failure! You did not guess any magic word.")
    print(HINT)

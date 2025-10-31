MAGIC_WORDS = set("cow", "pig", "chicken")  # set
HINT = "Hint: Try common farm animals."
SEP = ","

# Set maximum number of attempts
MAX_ATTEMPS = 5

# Initialize variables
num_attempts = 0
guessed_words = set()

# Ask the user to guess sequences of words
while num_attempts < MAX_ATTEMPS and guessed_words != MAGIC_WORDS:
    print("")
    user_input = input(f"Attempt {num_attempts + 1}/{MAX_ATTEMPS} - Enter words separated by commas: ")
    
    user_set = set()
    # Convert input into a set of cleaned words
    for word in user_input.split(SEP):
        cleaned_word = word.strip().lower()
        user_set.add(cleaned_word)
    #also: user_set = {word.strip().lower() for word in user_input.split(",")}

    # Update guessed words with any matches
    guessed_words = MAGIC_WORDS.intersection(user_set)

    # Feedback
    if guessed_words != MAGIC_WORDS:
        print(f"Matched: {len(guessed_words)} words")
        print("Keep trying!")

    # Increment attempts
    num_attempts = num_attempts + 1  


# Display results
if guessed_words == MAGIC_WORDS:
    print("Success! You guessed all magic words.")
    print("Magic words were:", MAGIC_WORDS)
    print("Attempts used:", num_attempts)
else:
    print("Failure! You did not guess all magic words.")
    print(HINT)
sentence = input()

# Initialize counters
word_count = 0
letter_count = 0

in_word = False  # Tracks if we are currently inside a word
# Iterate through each character in the sentence
for ch in sentence:
    # Count alphabetic characters (A–Z, a–z)
    if ('A' <= ch <= 'Z') or ('a' <= ch <= 'z'):
        letter_count += 1
        # If we find a letter and we are not already in a word, it's a new word
        if not in_word:
            word_count += 1
            in_word = True
    else:
        # Any non-letter character ends the current word
        in_word = False

# Display the results
print(word_count, letter_count)

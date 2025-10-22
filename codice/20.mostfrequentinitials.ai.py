# Get input from the user
user_sentence = input()

words = user_sentence.split()

initial_letter_counts = {}

if words: # Only proceed if there are words in the sentence
    for word in words:
        if word:  # Ensure the word is not an empty string
            initial_letter = word[0].lower()  # Get the first letter and convert to lowercase
            initial_letter_counts[initial_letter] = initial_letter_counts.get(initial_letter, 0) + 1

    most_frequent_letter = ''
    max_count = 0

    # Find the most frequent initial letter
    for letter, count in initial_letter_counts.items():
        if count > max_count:
            max_count = count
            most_frequent_letter = letter

    # Build the list of words starting with the most frequent initial letter
    result_words = []
    for word in words:
        if word and word[0].lower() == most_frequent_letter:
            result_words.append(word)

    print(result_words)
else:
    print("\nNo words found in the sentence.")
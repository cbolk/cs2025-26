CHARNUM = 26 # a - z

user_sentence = input()

#counters
frequencies = [0]*CHARNUM
wordsbyinitial = [[] for _ in range(CHARNUM)]

words = user_sentence.split()

if words: # Only proceed if there are words in the sentence
    #first word
    firstword = words[0]
    most_frequent_letter = firstword[0].lower()
    most_frequent_count = 1
    pos = ord(most_frequent_letter)-ord('a')
    frequencies[pos] = 1
    wordsbyinitial[pos].append(firstword)
    # remaining words
    for word in words[1:]:
        if word:  # Ensure the word is not an empty string
            initial_letter = word[0].lower()  # Get the first letter and convert to lowercase
            pos = ord(initial_letter)-ord('a')
            #add it to the correct group of words with the same initial 
            wordsbyinitial[pos].append(word)
            #keeping track of frequencies
            frequencies[pos] += 1 
            freqnum = frequencies[pos] 
            if freqnum > most_frequent_count:
                most_frequent_letter = initial_letter
                most_frequent_count = freqnum

    result_words = wordsbyinitial[ord(most_frequent_letter)-ord('a')]
    print(result_words)
else:
    print("\nNo words found in the sentence.")

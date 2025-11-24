DICTNAME = "dictionary.txt"

def find_anagrams(word, dicFilename):
    """
    Finds all proper words in dictionary.txt that are anagrams of the input. 
    """
    anagrams = []
    try:
        # Read dictionary file line by line
        dictionary = []
        with open(dicFilename, "r") as f:
            for line in f:
                line = line.strip().lower()
                if line != "":
                    dictionary.append(line)

        # Prepare letter-count dictionary for input word
        input_letters = {}
        for ch in word:
            if ch in input_letters:
                input_letters[ch] += 1
            else:
                input_letters[ch] = 1

        # Find anagrams
        for w in dictionary:
            if w != word:  # skip the same word

                # Count letters in w
                w_letters = {}
                for ch in w:
                    if ch in w_letters:
                        w_letters[ch] += 1
                    else:
                        w_letters[ch] = 1

                # Compare dictionaries
                if w_letters == input_letters:
                    anagrams.append(w)
    except FileNotFoundError:
        print("Error: dictionary.txt not found.")
    except Exception as e:
        print("Error:", e)
    return anagrams


# ---- MAIN FLOW -----

word = input("Enter a word: ").strip().lower()
anagrams = find_anagrams(word, DICTNAME)

# Display results
for a in anagrams:
    print(a)
print(len(anagrams))

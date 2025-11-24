DICTNAME = "dictionary.en.txt"
ASCIICHARS_SIZE = 256   # number of existing ASCII characters

def anagram_v2(word1, word2):
    # in python it is a single access
    counters = [0] * ASCIICHARS_SIZE
    for c in word1:
        counters[ord(c)] += 1
    # now I subtract the characters in word2 and 
    # as soon as I see a negative I have the answer
    for c in word2:
        counters[ord(c)] -= 1
        if counters[ord(c)] < 0:
            return False
    # need to check if there is a positive counter
    for count in counters:
        if count > 0:
            return False
    return True

def anagram_v1(word1, word2):
    counters = {}
    for c in word1:
        try:
            counters[c] += 1
        except: #the element is not in the dictionary yet
            counters[c] = 1
    # now I subtract the characters in word2 and 
    # as soon as I see a negative I have the answer
    for c in word2:
        try:
            counters[c] -= 1
        except: #the character is not in the dictionary - MISMATCH
            return False
        if counters[c] == 0:
            # remove it, so I do not have to check it later
            del counters[c]
        elif counters[c] < 0:
            return False
    # if there is never a mismatch, I need to see if there is a left over mismatching character
    return (counters == {})
    # in a different way
    # if counters != {}:    #characters left -- not an anagram
    #    return True
    #return False


def find_anagrams(word, dicFilename):
    anagrams = []

    try:
        with open(dicFilename) as fin:
            for line in fin:
                word_dic = line.strip().lower()
                if word != word_dic:
                    #in python is a single not expensive access
                    if len(word) == len(word_dic):
                        if anagram_v2(word, word_dic):
                            anagrams.append(word_dic)
    except FileNotFoundError:
        print(f"Error: {dicFilename} not found.")
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

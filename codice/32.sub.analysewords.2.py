STOP = ""
VOWELS = "aeiouAEIOU"
CONSONANTS = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"

def count_vowels(word):
    count = 0
    for letter in word:
        if letter in VOWELS:
            count += 1
    return count

def has_consonant_cluster(word):
    prev_is_consonant = False
    for letter in word:
        if letter in CONSONANTS:
            if prev_is_consonant:
                return True
            prev_is_consonant = True
        else:
            prev_is_consonant = False
    return False

def analyze_word(word):
    vowels = count_vowels(word)
    cluster = has_consonant_cluster(word)
    if vowels > 2 and not cluster:
        return "smooth"
    return "rough"


# Input
words_list = []
word = input()
while word != STOP:
    words_list.append(word)
    word = input()

# Output
print("You've inserted the following words:")
for word in words_list:
    result = analyze_word(word)
    print(f"{word}: {result}")


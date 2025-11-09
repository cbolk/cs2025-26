STOP = ""

def count_vowels(word):
    count = 0
    for letter in word:
        if letter in "aeiouAEIOU":
            count += 1
    return count

# Input loop
word = input()
while word != STOP:
    num_vowels = count_vowels(word)
    print(f"{word}: {num_vowels} vowels")
    word = input()

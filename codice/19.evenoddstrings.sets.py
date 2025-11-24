# Solution with two sets
STOPWORD = "stop"

odd_words = set()
even_words = set()

user_word = input("Enter a string (type 'stop' to finish): ")
user_word = user_word.strip()
while user_word != STOPWORD:    
    if len(user_word) % 2 == 0:
        even_words.add(user_word)
    else:
        odd_words.add(user_word)
    user_word = input("Enter a string (type 'stop' to finish): ")
    user_word = user_word.strip()

# Display results
print("Total unique strings:", len(odd_words) + len(even_words))
print("Total even-length unique strings:", len(even_words))
for word in even_words:
    print(word)
print("Total odd-length unique strings:", len(odd_words))
for word in odd_words:
    print(word)
    
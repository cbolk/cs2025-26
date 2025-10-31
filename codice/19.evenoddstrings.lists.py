# Solution with two lists
STOPWORD = "stop"

odd_sequence = [] 
even_sequence = []      

user_word = input("Enter a string (type 'stop' to finish): ")
user_word = user_word.strip()
while user_word != STOPWORD:    
    if len(user_word) % 2 == 0:
        even_sequence.append(user_word)
    else:
        odd_sequence.append(user_word)
    user_word = input("Enter a string (type 'stop' to finish): ")
    user_word = user_word.strip()
        
# display
print("Total strings:", len(odd_sequence) + len(even_sequence))
print("Total even-length strings:", len(even_sequence))
for word in even_sequence:
	print(word)
print("Total odd-length strings:", len(odd_sequence))
for word in odd_sequence:
    print(word)
    
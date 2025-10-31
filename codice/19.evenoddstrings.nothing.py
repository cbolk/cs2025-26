STOPWORD = "stop"

even_count = 0
odd_count = 0

user_word = input("Enter a string (type 'stop' to finish): ")
user_word = user_word.strip()
while user_word != STOPWORD:
    # check string len
    if len(user_word) % 2 == 0:
	    even_count += 1
	else:
	    odd_count += 1
    user_word = input("Enter a string (type 'stop' to finish): ")
    user_word = user_word.strip()
        
# display
print("Total strings: ", even_count+odd_count)
print("Even-length strings: ", even_count)
print("Odd-length strings: ", odd_count)

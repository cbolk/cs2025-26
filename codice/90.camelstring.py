seq = input()

# Initialize an empty string to build the result
result = ""

# Set a counter to distinguish odd and even positions
index = 0
# for each element in the string
for ch in seq:
    if index % 2 == 0:  #even
        result = result + ch.upper()
    else: # Odd position : lowercase
        result = result + ch.lower()
    index += 1

print(result)

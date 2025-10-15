seq = input()

size = len(seq)
i = size - 1  # Start from the last character
result = ""     # To build the final output

# Process characters from the end to the beginning
while i >= 0:
    ch = seq[i]
    count = 1
    i -= 1

    # Count how many times the same character repeats consecutively
    while i >= 0 and seq[i] == ch:
        count += 1
        i -= 1

    # convert integer into a string
    count_str = str(count)

    # Build result string
    result = result + ch + count_str

print(result)

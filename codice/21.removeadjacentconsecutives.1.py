NVAL = 10

num_sequence = []
valid = []
for i in range(NVAL):
    n = int(input(f"Insert number {i+1}: "))
    num_sequence.append(n)
    valid.append(True)

# Determine which indexes to remove
i = 0
while i < NVAL - 1:
    if abs(num_sequence[i] - num_sequence[i + 1]) == 1:
        # If two consecutive numbers differ by 1, must be removed both
        valid[i] = False
        valid[i + 1] = False
    i += 1

# Remove invalid numbers
i = 0
while i < NVAL:
    if not valid[i]:
        num_sequence.pop(i)
        valid.pop(i)
    else:
        i += 1

# Print result
print("Output:", num_sequence)

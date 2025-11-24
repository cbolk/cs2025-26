NVAL = 10

num_sequence = []
valid = []
for i in range(NVAL):
    n = int(input(f"Insert number {i+1}: "))
    num_sequence.append(n)
    valid.append(True)

# Determine which indexes to remove
i = 0
while i < NVAL - 1:  # must stop at NVAL-1 to avoid index error
     # If two consecutive numbers differ by 1, must be removed both
    if abs(num_sequence[i] - num_sequence[i + 1]) == 1:
        valid[i] = False
        valid[i + 1] = False
    i += 1

# Add valid number 
valid_sequence = []
i = 0
while i < NVAL:
    if valid[i]:
        valid_sequence.append(num_sequence[i])
    i += 1

print("Output:", valid_sequence)

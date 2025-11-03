
threshold = 2
# version 1
sequence = [1, 4, 6, -1, 4]
for i in range(len(sequence)):
	if sequence[i] < threshold:
		sequence[i] =  sequence[i] * sequence[i]
print(sequence)

# version 2
sequence = [1, 4, 6, -1, 4]
for elem in sequence:
	if elem < threshold:
		elem =  elem * elem
print(sequence)


sequence = []
# fill the list with relevant values
# ...

for i in range(len(sequence)):
	if sequence[i] < threshold:
		sequence[i] = sequence[i] * sequence[i]

for elem in sequence:
	if elem < threshold:
		elem = elem * elem

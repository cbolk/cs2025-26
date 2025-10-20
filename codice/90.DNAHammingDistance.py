seq1 = input()
seq2 = input()

sizee = len(seq1)
nmismatch = 0
for i in range(0, dim):
	if seq1[i] != seq2[i]:
		nmismatch += 1

print(nmismatch)
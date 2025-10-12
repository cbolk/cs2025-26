BASES = "ACGT"
BASESCOMP = "TGCA"

seq_in = input()

#for each element in seqin,
# find the corresponding complementary neuclotide: same position of element in BASESCOMP,
#concatenate
size = len(BASES)
reco_seq = ""
for elem in seq_in:
	# position in REF
	i = 0
	found = False
	while i < size and not found:
		if BASES[i] == elem:
			found = True
		else:
			i += 1
	comp_elem = BASESCOMP[i]
	# only complement
	# compseq = compseq + comp_elem
	reco_seq = comp_elem + reco_seq

print(reco_seq)

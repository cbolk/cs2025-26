seq_in = input()

#for each element in seqin,
#get the complement and
#concatenate
reco_seq = ""
for elem in seq_in:
	# position in REF
	if elem == 'A':
		comp_elem = 'T'
	elif elem == 'T':
		comp_elem = 'A'
	elif elem == 'C':
		comp_elem = 'G'
	#elif elem == 'C':
	else:
		comp_elem = 'C'

	reco_seq = comp_elem + reco_seq

print(reco_seq)

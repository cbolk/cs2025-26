def commoncharacter(seq1, seq2):
	for c in seq1:
		if c in seq2:
			return c
#	guaranteed to find one by problem constraints	
	return None
	
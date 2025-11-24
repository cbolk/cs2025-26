def commoncharacter(seq1, seq2):
    elem1 = set(seq1)
    elem2 = set(seq2)

    c = elem1.intersection(elem2)
	return c
    
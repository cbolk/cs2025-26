def compatiblestrings(seq1, seq2):
	size = len(seq1)

	if (size != len(seq2)):
		return False

    # Iterate through the strings character by character
    for i in range(size):
        # If characters are different and neither is a space, they are not compatible
        if seq1[i] != seq2[i] and seq1[i] != ' ' and seq2[i] != ' ':
            return False
    # If the loop completes, the strings are compatible
    return True

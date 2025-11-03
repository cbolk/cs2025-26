def compatible(seq1, seq2):
	dim = len(seq1)

	if len(seq2) != dim:
		# different size, they are not compatible
		comp = False
	else:
		# same size, investigate further
		# I assume they are compatible, look for a violation of the rule 

		# for every position in the strings
		for i in range(0, dim):
			# if the characters are different and neither of them is a space
				# the strings are not compatible
				# interrupt, we know the answer

		# if I got to the end without encountering a problem, the strings
		# are compatible

	#return the result

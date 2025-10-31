'''
Write a function that receives in input two strings, 
`seq` and `subs`, and computes and returns the number of times
`subs` appears in `seqs`, accepting overlapping.
'''

def countOccurrences(seq, subs):
	# from the beginning to the long sequence seq
	# to the last point where subs can start
	# AAACTCCTGCGACC ACAC
	#           ^
	# 
	dim_long = len(seq)
	dim_short = len(subs)
	lastpos = dim_long - dim_short + 1

	num = 0
	# for every slice in the long sequence of the 
	# same size of the subs
	for i in range(0, lastpos):
		# if the slice is equal to subs
		if seq[i:i+dim_short] == subs:
			# increment the counter
			num += 1

	return num


### FOR TESTING PURPOSES
longstring = "AATATATCGCGATATATTATATAAAA"
shortstring = "AT"

res = countOccurrences(longstring, shortstring)
print(res)

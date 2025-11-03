def replaceininterval(seq, fromc, toc, replc):
	newseq = ""
	# for every element in the string
	for elem in seq:
		# if it is included in the interval, boundaries included
		if elem >= fromc and elem <= toc:
#		if fromc <= elem <= toc:		
			# append the replacement character
			newseq += replc
		else:
			# append the original character
			newseq += elem
	return newseq

mystr = "this is a test for my function"
res = replaceininterval(mystr, 'c', 'm', 'x')
print(res)


ESEQ = "ACDEFGHKILMNPQRSTVYW"
namin = len(ESEQ)
counters = [0] * namin

pro = input()
size = len(pro)
# for each element in the ESEQ
for elem in pro:
	# find the position of the protein in ESEQ
	pos = ESEQ.find(elem)
	if pos >= 0: # we expect to find the elem
		# increment its corresponding counter
		counters[pos] += 1
	
# print out results
size = len(pro)
for i in range(0, namin):
	elem = ESEQ[i]
	# compute the ratio w.r.t. full length
	f = counters[i] / size	
	# print out the feq
	strOut = elem + “: “ + “ {0:.2f} %”.format(f*100) + “ (“ + str(counters[i]) + “)”
	print(strOut)


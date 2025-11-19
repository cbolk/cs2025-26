def loadData(fname):
	lst = []
	#open the file
	f = open(fname, "r")
	# for each line in the file
	for line in f:
		# gather the number
		num = int(line.strip())
		# if it is not already in the list
		if not num in lst:
			# add it
			lst.append(num)
	#close the file
	f.close()
	return lst

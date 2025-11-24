def loadData(fname):
	lst = []
	#open the file
	with open(fname, "r") as f:
	    # for each line in the file
        line = f.readline()
        while line != "":
            num = int(line.strip())
            # if it is not already in the list
            if not num in lst:
                # add it
                lst.append(num)
            line = f.readline()
	return lst
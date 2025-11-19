def loadData(fname):
	lst = []
	#open the file
	with open(fname, "r") as f:
        # for each line in the file
        lines = f.readlines()

        for elem in lines:
            num = int(elem.strip())
            # if it is not already in the list
            if not num in lst:
                # add it
                lst.append(num)

	return lst
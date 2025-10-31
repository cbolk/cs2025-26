def pairssumk(values, k):
	size = len(values)
	sumk = []
	posi = 0
	while posi < size:
		posj = posi + 1
		while posj < size:
			if values[posi] + values[posj] == k:
				pair = sorted([values[posi], values[posj]])
				if pair not in sumk:
					sumk.append(pair)
			posj += 1
		posi += 1
	return sumk

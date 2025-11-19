BASE = 10

def isHarshad(value):
	# copy to be used at the end
	dup = value

	sumdigit = value % BASE
	value = value / BASE
	while value > 0:
		sumdigit += value % BASE
		value = value / BASE
	if dup % sumdigit == 0:
		res = sumdigit
	else:
		res = 0
	return res

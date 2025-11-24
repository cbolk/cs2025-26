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

def rightTruncableHarshad(value):
	sumdigit = isHarshad(value) 
	while sumdigit > 0 and value > 0:
		value = value / BASE
		sumdigit = isHarshad(value)
	return (sumdigit > 0 and value == 0)
	
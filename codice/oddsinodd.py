FIXEDVALUE = 0

def oddsinodd(mylist):
	size = len(mylist)

	for i in range(0, size):
		if i % 2 == 1:
			if mylist[i] % 2 != 0:
				mylist[i] = FIXEDVALUE


# MAIN FLOW FOR TESTING PURPOSES
test = [1, 4, 7, -2, 6, 11, 10, 2, 8, 7]
oddsinodd(test)
print(test)

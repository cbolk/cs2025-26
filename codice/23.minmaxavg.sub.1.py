'''
Write a function that receives in input a list of integer values
and computes and returns the smallest, biggest and average value
of the elements in the list
'''

def minmaxavg(numberList):
	# initialise min max and total to the first element
	minval = numberList[0]
	maxval = numberList[0]
	tot = numberList[0]

	# for all elements in the list starting from the second one
	for elem in numberList[1:]:
		# check if I need to update either the max or the min
		if elem >= maxval:
			maxval = elem
		elif elem <= minval:
			minval = elem
		# add the element to the total
		tot += elem

	avg = tot / len(numberList)

	return minval, maxval, avg

## MAIN FLOW to TEST THE FUNCTION
values = [3, 4, -4, 12, 0, -4, 21, 43, 43, -43, 54, 3, 32, 54]
small, large, medium = minmaxavg(values)
print(small, large, medium)


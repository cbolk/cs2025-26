NVAL = 50

values = []		# empty list to store values
val = 0 		# accumulator for the total of the input values
for i in range(0, NVAL):
	val = int(input())
	values.append(val)
	tot += val

avg = tot / NVAL

# for each value in the list of values
for val in values:
	# if it is larger than the avg
	if val > avg:
		# display it
		print(val)
		
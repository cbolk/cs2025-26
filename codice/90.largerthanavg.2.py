NVAL = 50

values = []		# empty list to store values
for i in range(0, NVAL):
	val = int(input())
	values.append(val)

avg = sum(values) / NVAL	# it loops through all values 

# for each value in the list of values
for val in values:
	# if it is larger than the avg
	if val > avg:
		# display it
		print(val)
		
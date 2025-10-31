STOPVAL = 0

def minmaxavg(l):
	minval = maxval = tot = l[0]
	for elem in l[1:]:
		tot += elem
		if elem <= minval:
			minval = elem
		elif elem > maxval:
			maxval = elem

	avgval = tot / len(l)

	return minval, maxval, avgval

#main flow
values = []

num = int(input())
while val != STOPVAL:
	values.append(val)
	num = int(input())

small, big, avg = minmaxavg(values)
print(small, big, avg)

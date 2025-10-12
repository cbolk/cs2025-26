# CONSTANT / ARBITRARY ASPECTS OF THE SOLUTION
STOP = 0

val = int(input())
minv = val
maxv = tot = val
nval = 1

val = int(input())
while val != STOP:
	tot += val
	if val > maxv:
		maxv = val
	elif val < minv:
		minv = val
	nval += 1
	val = int(input())

avgv = tot / nval
print(minv, maxv, avgv)

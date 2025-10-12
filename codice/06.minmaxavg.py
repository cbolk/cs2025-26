# CONSTANT / ARBITRARY ASPECTS OF THE SOLUTION
NVAL = 35

val = int(input())
minv = val
maxv = tot = val

i = 1
while i < NVAL:
	val = int(input())
	tot += val
	if val >= maxv:
		maxv = val
	elif val < minv:
		minv = val
	i += 1

avgv = tot / NVAL
print(minv, maxv, avgv)

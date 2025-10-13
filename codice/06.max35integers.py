# CONSTANT / ARBITRARY ASPECTS OF THE SOLUTION
NVAL = 35

val = int(input())
maxval = val

count = 1
while count < NVAL:
	val = int(input())
	if val >= maxval:
		maxval = val
	count += 1

print(maxval)
STOP = 0
FNAME = "primes.txt"

def prime(n):
	# 1 and even numbers greater than 2 are not prime
	if (n == 1) or (n % 2 == 0 and n > 2):
		return False
	div = 3
	while div * div <= n:
		if n % div == 0:
			return False
		else:
			div += 2
	return True

with open(FNAME, "w") as fout:
	val = int(input())
	while val != STOP:
		if prime(val):
			#write the number and add the newline after it
			fout.write(str(val) + "\n")
		val = int(input())


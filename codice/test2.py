fromval = int(input())
toval = int(input())
# for each number in my interval
for val in range(fromval,toval+1):
	# compute if it is a prime number
	# val contains the value we have to verify 
	if val == 1 or (val % 2 == 0 and val != 2) :
		isprime = False
	else:
		isprime = True
		div = 3
		for div in range(3, val/2, )
#		while div*div < val and (isprime == True):
			rem = val % div
			if rem == 0:
				isprime = False
			else:
				div += 2
	# if it is a prime number
	if isprime == True:		# if isprime:
		# display it
		print(val)

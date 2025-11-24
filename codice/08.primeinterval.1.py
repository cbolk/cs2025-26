fromval = int(input())
toval = int(input())
# for each number in my interval
val = fromval
while val <= toval:
	# compute if it is a prime number
	# val contains the value we have to verify 
	if val == 1:
		isprime = False
	else:
		isprime = True
		div = 2
		while div < val and (isprime == True):
			rem = val % div
			if rem == 0:
				isprime = False
			else:
				div += 1
	# if it is a prime number
	if isprime == True:		# if isprime:
		# display it
		print(val)
	val += 1	# next number to be processed
#end

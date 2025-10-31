 CONSTANTS 

# FUNCTIONS
''' 
function that asks the user a strictly positive integer, repeating the request till the value meets the requirements. 
the function returns the value to the caller
'''
def getPositive():
	val = int(input())
	while val <= 0:
		val = int(input())
	return val

''' 
funciton that asks the user an integer included in an interval, boundaries included. 
it repeats the request till the value meets the requirements
the function returns the value to the caller
'''
def getInsideInterval(lowerBound, upperBound):
	val = int(input())
	while val < lowerBound or val > upperBound:
		val = int(input())
	return val

''' 
function that receives in input a positive integer (for sure) and computes and returns its factorial
'''
def factorial(value):
	f = 1
	i = value
	while i > 1:
		f = f * i
		i -= 1
	return f

# MAIN FLOW
# THE TASK THE PROGRAM PERFORM TO SOLVE THE PROBLEM
# controlled acquisition n (strictly positive)
n = getPositive()

# controlled acquisition k (included in interval [1, n])
k = getInsideInterval(1, n)

# factorial n
fn = factorial(n)
# factorial k
fk = factorial(k)
# factorial n-k
diff = n-k
fnk = factorial(diff)
# combinations
comb = fn // (fk * fnk)

print(comb)
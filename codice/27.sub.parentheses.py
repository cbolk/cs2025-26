OPEN = '('
CLOSE = ')'

def validateParentheses (seq):

	#number of open parentheses
	num = 0
	# for every element, increment/decrement the number of open parentheses
	for elem in seq:
		if elem == OPEN:
			num += 1
		elif elem == CLOSE:
			num -= 1
		# if there are more closed parentheses than open ... validation False
		if num < 0:
			return False

	# there is an unbalanced open parentheses
	if num > 0:
		return False
		
	# all parentheses are balanced
	return True

ISCON = 'C'
ISVOW = 'V'
ISDIG = 'D'
VOWELS = "aeiou"

seq = input()
check = input()

i = 0
isok = True
for elem in seq:
	if elem in VOWELS:
		if check[i] != ISVOW:
			isok = False
	elif elem >= '0' and elem <= '9': # elem in DIGITS
		if check[i] != ISDIG:
			isok = False
	else:
		if check[i] != ISCON:
			isok = False
	if isok == False:
		break
	else:
		i = i + 1	
print(isok)
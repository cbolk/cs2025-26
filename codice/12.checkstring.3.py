ISCON = 'C'
ISVOW = 'V'
ISDIG = 'D'
VOWELS = "aeiou"

seq = input()
check = input()

i = 0
isok = True
for elem in seq:
	if (elem in VOWELS and check[i] != ISVOW) or 
	   (elem >= '0' and elem <= '9' and check[i] != ISDIG) or
	   (elem >= 'a' and elem <= 'z' and elem not in VOWELS and check[i] != ISCON):
	   isok = False
	   break
	else:
		i = i + 1

print(isok)
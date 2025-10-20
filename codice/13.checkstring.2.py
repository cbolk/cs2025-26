ISCON = 'C'
ISVOW = 'V'
ISDIG = 'D'
VOWELS = "aeiou"

seq = input()
check = input()

size = len(seq)
isok = True
for i in range(0, size):
	if (seq[i] in VOWELS and check[i] != ISVOW) or 
	   (seq[i] >= '0' and seq[i] <= '9' and check[i] != ISDIG) or
	   (seq[i] >= 'a' and seq[i] <= 'z' and seq[i] not in VOWELS and check[i] != ISCON):
	   isok = False
	   break

print(isok)
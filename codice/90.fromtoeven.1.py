BASE = 10

start = int(input())
end = int(input())

if (start+1 % 2) == 1:	/* if it is odd, it does not have all even digits */
	start += 1

i = start
while i < end:
	num = i
	all_even = True
	while (num > 0) and all_even:
		digit = num % BASE
		if digit % 2 != 0:
			all_even = False
		num //= BASE
	if all_even:
		print(i)
	i += 2
	
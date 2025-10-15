seq = input()
ch = input()

count = 0
for el in seq:
	if el == ch:
		count += 1

print(count)
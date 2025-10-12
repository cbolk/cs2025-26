STOP = 0

count_e = 0
count_o = 0

n = int(input())
while n != STOP:
	if n % 2 == 0:
		count_e += 1
	else:
		count_o += 1
	n = int(input())

count = count_e + count_o
print(count_e, count_o, count)

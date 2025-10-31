seq = input().strip()
sep = input().strip()
size = int(input().strip())

values = seq.split(sep)
numbers = {}
for val in values:
	num = int(val)
	if val in numbers:
		numbers[val] += 1
	else:
		numbers[val] = 1

sorted_list = sorted(numbers.items(), key=lambda x: x[1])

for i in range(0, size):
	print(sorted_list[i][0])

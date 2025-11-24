STOP = 0

numbers = []

value = int(input())
while value != STOP:
	if value not in numbers:
		numbers.append(value)
	value = int(input())

sorted_numbers = sorted(numbers, reverse=True)
print(sorted_numbers)

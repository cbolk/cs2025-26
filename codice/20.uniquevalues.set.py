STOP = 0

numbers = set()

value = int(input())
while value != STOP:
	numbers.add(value)
	value = int(input())

sorted_numbers = sorted(numbers, reverse=True)
print(sorted_numbers)

val1 = int(input())
val2 = int(input())

# store in variable small the smallest value 
# and in variable big the higher one
if val1 >= val2:
	small = val2
	big = val1
else:
	small = val1
	big = val2

print(small, big)

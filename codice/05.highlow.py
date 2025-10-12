val1 = int(input("insert an integer: "))
val2 = int(input("insert an integer: "))

if val1 > val2:
	low = val2
	high = val1
else:
	low = val1
	high = val2
print(low, high)

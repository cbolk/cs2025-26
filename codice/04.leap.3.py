year = int(input("insert an integer: "))

if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
	isleap = True
else:
	isleap = False

print(isleap)

year = int(input("insert an integer: "))

if year % 4 == 0:
	if year % 100 != 0:
		isleap = True
	elif year % 400 == 0:
		isleap = True
	else:
		isleap = False
else:
	isleap = False

print(isleap)

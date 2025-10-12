str_in = input()

str_out = ""
size = len(str_in)

i = size - 1
while i >= 0:
	str_out = str_out + str_in[i]
	i -= 1

print(str_out)
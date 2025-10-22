SEP = ","

seq = input()

temp_str = seq.split(SEP)

temps = []
tot = 0
for ts in temp_str:
	t = float(ts.strip())
	temps.append(t)
	tot += t

size = temps.len()
half = size // 2 
temps.sort()
if size % 2 == 1:
	median = temps[half]
else:
	median = (temps[half-1] + temps[half]) / 2
avg = tot / size

print(median, avg)


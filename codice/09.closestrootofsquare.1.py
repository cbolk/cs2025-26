val = int(input())

# check all values such that their square is smaller than val
if val == 1:
	sq = 1
else:
	sq = 1
	while sq * sq < val:
		sq += 1
	sq -= 1

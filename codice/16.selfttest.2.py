seq = input()
longseq = input()

for elem in seq:
	if elem in longseq:
		allfound = True
	else:
		allfound = False


print(allfound)
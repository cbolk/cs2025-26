seq = input()
longseq = input()

allfound = True
for elem in seq:
	if elem not in longseq:
		allfound = False
		break

print(allfound)

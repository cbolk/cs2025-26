seq = input()
oldc = input()
newc = input()

newseq = ""
for el in seq:
	if el == oldc:
		newseq = newseq + newc
	else:
		newseq = newseq + el


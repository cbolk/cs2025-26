seq = input()
oldc = input()
newc = input()

newseq = ""
for c in seq:
	if c == oldc:
		newseq = newseq + newc
	else:
		newseq = newseq + c

print(newseq)

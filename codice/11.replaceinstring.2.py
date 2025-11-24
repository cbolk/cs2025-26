seq = input()
oldc = input()
newc = input()

newseq = ""
for el in seq:
	if el == oldc:
		addch = newc
	else:
		addch = el
	newseq = newseq +addch 

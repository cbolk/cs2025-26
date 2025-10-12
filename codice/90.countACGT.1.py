ELEMS = "ACGT"

dnaseq = input()

na = 0
nc = 0
ng = nt = 0

for e in dnaseq:
		if e == "A":
			na += 1
		elif e == "C":
			nc += 1
		elif e == "G":
			ng += 1
		else: #T
			nt += 1

print(na, nc, ng, nt)

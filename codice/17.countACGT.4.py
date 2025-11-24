ELEMS = "ACGT"

dnaseq = input()

# dictionary initialisation
count = {}
for e in ELEMS:
	count[e] = 0


for e in dnaseq:
	count[e] = count[e]+1

for k, v in count.items():
	print(v, end=" ")
print(" ")
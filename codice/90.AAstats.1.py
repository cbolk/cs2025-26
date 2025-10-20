ESEQ = "ACDEFGHKILMNPQRSTVYW"

pro = input()
size = len(pro)
# for each element in the ESEQ
for e in ESEQ:
	# count how many times the element appear in pro
	num = 0
	for j in range(0, size):
		if pro[j] == e:
			num += 1

	# compute the ratio w.r.t. full length
	freq = num / size
	strOut = e + “: “ + “ {0:.2f} %”.format(freq*100) + “ (“ + str(num) + “)”

# print out the feq
print(strOut)

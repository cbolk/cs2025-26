def replicate(seq, nrep):
	if nrep % 2 == 0:
		seq = seq * nrep
	else:
		seq = seq
	print(seq)


def reduce(seq, part):
	size = len(seq) // 2
	if size % 2 != 0:
		seq = seq[0:size]
	else:
		seq = seq[size:]
	print(seq)
	return seq

#main flow
sentence = input()
times = int(input())

replicate(sentence, times)
print(sentence)
print("*********")
sentence = reduce(sentence, times)
print(sentence)

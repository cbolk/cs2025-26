STOP = ""

frequencies = []

word = input()
if word != STOP:
	maxfword = word
	maxfreq = 1
	frequencies.append([word, 1])
	word = input()
	while word != STOP:
		found = False
		for pair in frequencies:
			if pair[0] == word:
				found = True
				pair[1] = pair[1]+1
				break
		if found:
			num = pair[1]
		else:
			num = 1
			frequencies.append([word, num])

		if num > maxfreq:
			maxfword = word
			maxfreq = num
		#next word
		word = input()
else:
	maxfword = ""
	maxfreq = 0
print(maxfword, maxfreq)
STOP = ""

frequencies = {}

word = input()
if word != STOP:
	maxfword = word
	maxfreq = 1
	frequencies[word] = 1
	word = input()
	while word != STOP:
		#increment frequencies
		if word in frequencies.keys():
			num = frequencies[word] + 1
		else:
			num = 1
		frequencies[word] = num
		if num > maxfreq:
			maxfword = word
			maxfreq = num
		#next word
		word = input()
else:
	maxfword = ""
	maxfreq = 0
print(maxfword, maxfreq)
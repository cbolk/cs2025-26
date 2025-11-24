def isanagram(word1, word2):
	size1 = len(word1)
	size2 = len(word2)

	if size1 == size2:
		used = [0]*size1
		res = True		# assume it is an anagram and find if there is a violation of the rule
		for ch in word2:
			found = False
			i = 0
			while i < size1 and not found:
				if word1[i] == ch and used[i] == 0:
					found = True
					used[i] = 1
				i += 1
			if not found:
				res = False
				break
	else:
		res = False
	return res

# MAIN FLOW
word_anagrams = {}
latest_word = input().strip()
while latest_word != "":
	# search if there is already an anagram of the new word in the collection
	added = False
	for element in word_anagrams:
		if isanagram(latest_word, element):
#			anagrams = word_anagrams[element]
			word_anagrams[element].append(latest_word)
			added = True
			break
	if not added:
		# at present there is no anagram of the present word
		word_anagrams[latest_word] = []

	# next entry
	latest_word = input().strip()

print(word_anagrams)

for word, anagrams in word_anagrams.items():
	print(word, end=" ")
	for a in anagrams:
		print(a, end= " ")
	print()


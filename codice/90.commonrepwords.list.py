# first collection
seq1 = input().strip().split()
# second collection
seq2 = input().strip().split()

# create set of words that appear more than once in the first list
dup_seq1 = []
# for every word in the list
pos = 0
for word in seq1:
    # if word has another entry in the rest of the list
    if word in seq1[pos+1:]:
        # if it has not been found yet (and added to the list of repeated words)
        if word not in dup_seq1:
            dup_seq1.append(word)
    pos += 1

# the same with the second collection
dup_seq2 = []
pos = 0
for word in seq2:
    # if word has another entry in the rest of the list
    if word in seq2[pos+1:]:
        # if it has not been found yet (and added to the list of repeated words)
        if word not in dup_seq2:
            dup_seq2.append(word)
    pos += 1

# the words common to both lists
common_rep_words = []
for word in dup_seq1:
    if word in dup_seq2:
        common_rep_words.append(word)

# display
for word in common_rep_words:
    print(word, end=" ")
print()
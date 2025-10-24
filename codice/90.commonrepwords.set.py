# first collection
seq1 = input().strip().split()
# second collection
seq2 = input().strip().split()

# create set of words that appear more than once in the first list
# exploit set unique element property and later the intersection
dup_seq1 = set()
# for every word in the list
pos = 0
for word in seq1:
    # if word has another entry in the rest of the list
    if word in seq1[pos+1:]:
        dup_seq1.add(word)
    pos += 1

# the same with the second collection
dup_seq2 = set()
pos = 0
for word in seq2:
    # if word has another entry in the rest of the list
    if word in seq2[pos+1:]:
        # if it has not been found yet (and added to the list of repeated words)
        dup_seq2.add(word)
    pos += 1

# intersection of the words common to both sets
common_rep_words_set = dup_seq1.intersection(dup_seq2)
# or 
# common_rep_words_set = dup_seq2.intersection(dup_seq1)

common_rep_words = list(common_rep_words_set)

# display
for word in common_rep_words:
    print(word, end=" ")
print()

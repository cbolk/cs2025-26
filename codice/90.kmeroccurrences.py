text = input("text: ")
kmer = input("k-mer: ")

num = 0
tsize = len(text)
ksize = len(kmer)
stop = tsize - ksize + 1
for i in range(0, stop):
    equal = 1
    j = 0
    while j < ksize and equal:
        if text[i+j] != kmer[j]:
            equal = 0
        j += 1
    num += equal

print(num)

def getkmers(seq):
    tdim = len(seq)
    #the last position where a kmer can start
    lastpos = tdim - k + 1
    #the list of kmers
    kmers = []
    for i in range(0, lastpos):
        # take a subsequence of length k of adjacent elements
        elem = seq[i:i+k]
        # if it is not already part of the list, insert it
        if elem not in kmers:
            kmers.append(elem)

    return kmers

## MAIN FLOW
text = input()
k = int(input())

# extract all possible k-mers
kmerlist = getkmers(text)
# number of k-mers
numkmers = len(kmerlist)

freqpatterns = [kmerlist[0]]
maxfreq = countexact(text, freqpatterns[0])


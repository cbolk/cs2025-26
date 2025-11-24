dnaseq = input()
k = int(input())

#added to remove eventual spaces on the command line
dnaseq = dnaseq.strip()

# extract all possible k-mers
tdim = len(dnaseq)
lastpos = tdim-k+1
kmers = set()
for i in range(0, lastpos):
    # take a subsequence of length k of adjacent elements
    elem = dnaseq[i:i+k]
    # if it is not already part of the list, insert it
    kmers.add(elem)

kmers_sorted = sorted(kmers)

for km in kmers_sorted:
    print(km, end=" ")
print("")
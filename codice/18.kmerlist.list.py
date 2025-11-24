dnaseq = input()
k = int(input())

#added to remove eventual spaces on the command line
dnaseq = dnaseq.strip()

# extract all possible k-mers
tdim = len(dnaseq)
lastpos = tdim-k+1
kmers = []
for i in range(0, lastpos):
    # take a subsequence of length k of adjacent elements
    elem = dnaseq[i:i+k]
    # if it is not already part of the list, insert it
#    if elem not in kmers:
    kmers.append(elem)

#kmers.sort()

for km in kmers:
    print(km, end=" ")
print()
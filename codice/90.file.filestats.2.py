filename = input().strip()
with open(filename, "r") as fin:
    nlines = 0
    nc = 0
    for line in fin:
        nc += len(line)
        nlines += 1
print(nlines, nc)


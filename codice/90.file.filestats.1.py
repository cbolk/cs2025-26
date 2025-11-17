filename = input().strip()
with open(filename, "r") as fin:
    lines = fin.readlines()
    nlines = len(lines)
    nc = 0
    for line in lines:
        nc += len(line)
print(nlines, nc)

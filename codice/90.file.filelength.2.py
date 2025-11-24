filename = input().strip()
with open(filename, "r") as fin:   
    dim = 0 
    c = fin.read(1)
    while c:
        print(c, end="")
        dim += 1
        c = fin.read(1)
print(dim)

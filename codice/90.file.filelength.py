filename = input().strip()
with open(filename, "r") as fin:
    text = fin.read()
    dim = len(text)
print(dim)

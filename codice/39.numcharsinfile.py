# get the name of the file
# remove possible trailing spaces at the end
filename = input().strip()

# unique read operation
# everything is stored in a string
with open(filename, "r") as fin:
    text = fin.read()
    dim = len(text)
print(dim)

# read one character at the time
with open(filename, "r") as fin:
	dim = 0
    c = fin.read(1)	#read one character
    while c:	# while I have read something
    	dim += 1
    	c = fin.read(1)
print(dim)
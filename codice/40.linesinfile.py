# get the name of the file
# remove possible trailing spaces at the end
filename = input().strip()

with open(filename) as fin:
    numlines = 0
    for line in fin:
        numlines += 1

    print(numlines)


## using statement readline() instead of for 
with open(filename) as fin:
    numlines = 0
    line = fin.readline()
    while line:
        numlines += 1
        line = fin.readline()
    print(numlines)

## reading all lines in a single operation
with open(filename) as fin:
    lines = fin.readlines()
    #lines = ["content of the first line", "content 2nd line"]
    numlines = len(lines)
    print(numlines)

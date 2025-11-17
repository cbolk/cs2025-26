STOP = 0

fnameodd = input()
fnameeven = input()

with open(fnameodd, "w") as fodd:
    with open(fnameeven, "w") as feven:
        nodd = 0
        neven = 0
        val = int(input())
        while val != STOP:
            if val % 2 == 1:
                fodd.write(str(val) + "\n")
                nodd += 1
            else:
                feven.write(str(val) + "\n")
                neven += 1
            val = int(input())

print(nodd, neven)

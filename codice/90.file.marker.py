def countmarkers(filename, marker):
    try:
        res = 0
        with open(filename, "r") as filein:
            for line in filein:
                if marker in line.strip(): # useless to keep counting line.strip().count(marker) > 0:
                    res += 1

    except FileNotFoundError:
        res = -1
    except:
        res = -1
    return res

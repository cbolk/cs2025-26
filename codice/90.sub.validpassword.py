def validPassword(pwd):
    dim = len(pwd)

    hasCap = pwd[0].isupper()
    hasSmall = pwd[0].islower()
    hasDigit = pwd[0].isdigit()
    adjacentEqual = False
    i = 1
    while i < dim and not (hasCap and hasSmall and hasDigit):
        if not hasCap and pwd[i].isupper():
            hasCap = True
        if not hasSmall and pwd[i].islower():
            hasSmall = True
        if not hasDigit and pwd[i].isdigit():
            hasDigit = True
        if pwd[i-1] == pwd[i]:
            adjacentEqual = True
            break
        i += 1

    #why am I here?
    result = hasCap and hasSmall and hasDigit and not adjacentEqual
    return results
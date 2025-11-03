JOLLY = ' '

def compatible(seq1, seq2):
    dim = len(seq1)

    if len(seq2) != dim:
        # different size, they are not compatible
        comp = False
    else:
        # same size, investigate further
        # I assume they are compatible, look for a violation of the rule 
        comp = True
        # for every position in the strings
        for pos in range(0, dim):
            # if the characters are different and neither of them is a space
            if seq1[pos] != seq2[pos] and (seq1[pos] != JOLLY and seq2[pos] != JOLLY):
#           if seq1[pos] != seq2[pos] and not(seq1[pos] == JOLLY or seq2[pos] == JOLLY):
                # the strings are not compatible
                comp = False
                break
                # interrupt, we know the answer
        # if I got to the end without encountering a problem, the strings
        # are compatible
    #return the result
    return comp

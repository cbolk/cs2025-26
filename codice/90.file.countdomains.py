HEADERSTART = '>'

def getSequencesWithDomains(filename, domains):
    res = []
    try:
        with open(filename, "r") as filein:
            # number of domains
            num = len(domains)
            # list of sequences to be returned
            #read the header
            line = filein.readline().strip()
            while line and line[0] == HEADERSTART:
                seqname = line[1:]  #name of the sequence
                #read the entire sequence 
                seq = ""
                line = filein.readline().strip()
                while line and line[0] != HEADERSTART:
                    seq += line
                    line = filein.readline().strip()
                # the sequence is concluded
                # check if all domains are in
                allin = domains[0] in seq
                d = 1
                while allin and d < num:
                    if not domains[d] in seq:
                        allin = False
                    else:
                        d += 1
                if allin:
                    res.append(seqname)
            # no more lines
    except FileNotFoundError:
        print(f"problems accessing file {filename}")
    return res
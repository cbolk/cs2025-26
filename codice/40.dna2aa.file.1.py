FILENAME = "codonAAtable.csv"
SEP = ","

DNAELEM = 'T'
RNAELEM = 'U'
CODON_SIZE = 3
END = "Stop"
ERROR = "Error"

def loadcodontableshort(fname, separator):
    codon_dic = {}
    with open(fname, 'r') as fin:
        #first line contains the header
        strheader = fin.readline()
        #all the remaining lines have the corresponding values
        for line in fin:
            parts = line.strip().split(separator)
            codon = parts[0]
            aa = parts[3]
            codon_dic[codon] = aa
            # or directly
            # codon_dic[parts[0]] = parts[3]
    return codon_dic

def codon2aa(seq, d):
    dim = len(seq)

    # create an empty result string
    aaseq = ""
    # for each codon (sequence of three elements)
        # find the corresponding encoding
        # append it to the result
    pos = 0
    last_pos = dim - CODON_SIZE
    while pos < last_pos:
        codon = seq[pos:pos+CODON_SIZE]
        try:
            aa = d[codon]
            aaseq += aa
            pos += CODON_SIZE
        except:
            print(f"codon {codon} not found")
            return aaseq + ERROR
    aaseq += END
    return aaseq

# MAIN FLOW
# ask the user the DNA string
dnaseq = input()
# convert into the RNA strand
rnaseq = dnaseq.replace(DNAELEM, RNAELEM)
d = loadcodontableshort(FILENAME, SEP)
aastring = codon2aa(rnaseq, d)
print(aastring)

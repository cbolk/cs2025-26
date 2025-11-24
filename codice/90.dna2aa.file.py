DNAELEM = 'T'
RNAELEM = 'U'
CODON_SIZE = 3
END = "Stop"
ERROR = "Error"
SEP = ","

def loadcodontableshort(fname):
    codon_dic = {}
    try: 
        with open(fname, 'r', newline='') as infile:
            for line in infile:
                parts = line.strip().split(SEP)
                codon_dic[parts[0]] = parts[3]
    except:
        print(f"File {fname} not accessible")
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
# load the file with the mapping
filename = input()
# convert into the RNA strand
rnaseq = dnaseq.replace(DNAELEM, RNAELEM)
d = loadcodontableshort(filename)
if d:
    aastring = codon2aa(rnaseq, d)
    print(aastring)

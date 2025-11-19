DNAELEM = 'T'
RNAELEM = 'U'
CODON_SIZE = 3
END = "Stop"
ERROR = "Error"

GENETIC_CODE_1 = {
    'UUU': 'F', 'UUC': 'F', 'UUA': 'L', 'UUG': 'L',
    'UCU': 'S', 'UCC': 'S', 'UCA': 'S', 'UCG': 'S',
    'UAU': 'Y', 'UAC': 'Y', 'UAA': '*', 'UAG': '*',
    'UGU': 'C', 'UGC': 'C', 'UGA': '*', 'UGG': 'W',
    'CUU': 'L', 'CUC': 'L', 'CUA': 'L', 'CUG': 'L',
    'CCU': 'P', 'CCC': 'P', 'CCA': 'P', 'CCG': 'P',
    'CAU': 'H', 'CAC': 'H', 'CAA': 'Q', 'CAG': 'Q',
    'CGU': 'R', 'CGC': 'R', 'CGA': 'R', 'CGG': 'R',
    'AUU': 'I', 'AUC': 'I', 'AUA': 'I', 'AUG': 'M',
    'ACU': 'T', 'ACC': 'T', 'ACA': 'T', 'ACG': 'T',
    'AAU': 'N', 'AAC': 'N', 'AAA': 'K', 'AAG': 'K',
    'AGU': 'S', 'AGC': 'S', 'AGA': 'R', 'AGG': 'R',
    'GUU': 'V', 'GUC': 'V', 'GUA': 'V', 'GUG': 'V',
    'GCU': 'A', 'GCC': 'A', 'GCA': 'A', 'GCG': 'A',
    'GAU': 'D', 'GAC': 'D', 'GAA': 'E', 'GAG': 'E',
    'GGU': 'G', 'GGC': 'G', 'GGA': 'G', 'GGG': 'G'
}

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
        if codon in d:
            aa = d[codon]
            aaseq += aa
            pos += CODON_SIZE
        else:
            print(f"codon {codon} not found")
            return aaseq + ERROR
    aaseq += END
    return aaseq

# MAIN FLOW
# ask the user the DNA string
dnaseq = input()
# convert into the RNA strand
rnaseq = dnaseq.replace(DNAELEM, RNAELEM)
aastring = codon2aa(rnaseq, GENETIC_CODE_1)
print(aastring)
BASE = 10
SYMBOL = "#"

def eval_digits_frequency(value):
    """Return (freq, ndigits) for the non-negative integer value."""
    freq = [0] * BASE
    digit = value % BASE
    freq[digit] +=1
    ndigits = 1
    value = value // BASE
    while value > 0:
        digit = value % BASE
        freq[digit] +=1
        ndigits += 1
        value = value// BASE

    return freq, ndigits


def display_histogram(freq):
    """Print horizontal histogram lines only for digits with non-zero counts."""
    for d in range(BASE):
        count = freq[d]
        if count > 0:
            print(f"{d}:", SYMBOL * count)


# ---- Main program  ----

# Inputs
seq_values = []
freqs_list = [0] * BASE
total_digits = 0

v = int(input())
while v >=0:
    seq_values.append(v)
    v = int(input())

# Evaluate frequencies for each value
for val in seq_values:
    val_freqs, ndigits = eval_digits_frequency(val)
    total_digits += ndigits
    for i in range(BASE):
        freqs_list[i] += val_freqs[i]


if len(seq_values)==0:
    print("No integers inserted")
else:  
    # Print histogram  
    display_histogram(freqs_list)
    # Calculate and print average number of digits
    average = total_digits / len(seq_values)
    print("Digits average:", average) 

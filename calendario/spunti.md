---
exe-start: 1
---

# Exercizes


::: exefatti

Given a list `values` and a positive integer `k`, find the first negative integer for each and every _window_ (contiguous sublist) of size `k`. If a window does not contain a negative integer, then 0 is element corresponding to the window.

Examples:
```
input: values = [-8, 2, 3, -6, 10], k = 2
output: [-8, 0, -6, -6]
```

+ _window_ [-8, 2] First negative integer is -8.
+ _window_ [2, 3] No negative integers, output is 0.
+ _window_ [3, -6] First negative integer is -6.
+ _window_ [-6, 10] First negative integer is -6.

```
input: values = [12, -1, -7, 8, -15, 30, 16, 28], k = 3
output: [-1, -1, -7, -15, -15, 0] 
```

+ _window_ [12, -1, -7] First negative integer is -1.
+ _window_ [-1, -7, 8] First negative integer is -1.
+ _window_ [-7, 8, -15] First negative integer is -7.
+ _window_ [8, -15, 30] First negative integer is -15.
+ _window_ [-15, 30, 16] First negative integer is -15.
+ _window_ [30, 16, 28] No negative integers, output is 0.

Input: arr[] = [12, 1, 3, 5] , k = 3
Output: [0, 0] 
Explanation:
Window [12, 1, 3] No negative integers, output is 0.
Window [1, 3, 5] No negative integers, output is 0.


:::

::: exefatti
Write a function called `most_occur(c, words)` that takes a single character `c` and a list of one or more strings called `words` and returns the string in the list with the most occurrences of `c`. In case more than a single word ties for the number of occurrences, you can decide which one to return.

Examples:
```
input: c = "a", words = ["able", "banana", "mama", "tiger", "channel"]
output: "banana"

input: c = "o", words = ["look", "over", "there"]
output: "look"
```

```python
def most_occur(c, words):
	nwords = len(words)

    # Initialise with the first word
    max_word = words[0]
    max_count = words[0].count(c)

    # Iterate through the rest of the words and compare
    # from the second word
    for i in range(1, nwords):
        current_word = words[i]
        current_count = current_word.count(c)
        if current_count > max_count:
            max_count = current_count
            max_word = current_word

    return max_word
```


:::


::: exefatti

Write a function `smaller_of` that takes as inputs two lists `vals1` and `vals2` and constructs and returns a new list in which each element is the the smaller of the corresponding elements from the original lists. If the two elements for a given position have the same value, you should include that value. For example:

```
input: vals1 = [3, 4, 9, 5], vals2 = [7, 2, 0, 5]
output: [3, 2, 0, 5]
```

```python 
def smaller_of(vals1, vals2):
	size = len(vals1)

	result = []
	for i in range(0, size):
		if vals1[i] < vals2[i]:
			result.append(vals1[i])
		else:
			result.append(vals2[i])
	return result
```

```python 
def smaller_of(vals1, vals2):
	size = len(vals1)

	result = []
	for i in range(0, size):
		result.append(min(vals1[i], vals2[i]))
	return result
```

```python 
def smaller_of(vals1, vals2):
	size = len(vals1)
	result = [min(vals1[i], vals2[i]) for i in range(0, size)]
	return result
```
:::

::: exefatti

Write a function `mergestrings` that takes as inputs two strings `s1` and `s2` and creates and returns a new string that is formed by _merging_ together the characters in the strings `s1` and `s2` to create a single string, by adhering to the following rules:

+ if `s1` and `s2` have the same character at a given position, it should be included once in the returned string.

+ if `s1` and `s2` have different characters at a given position, both characters should be included in the returned string: first the character from `s1`, then the character from `s2`.

Example:
```
input: "abcde" "abghe"
result: "abcgdhe"
```

```python
def mergestrings(s1, s2):
	dim1 = len(s1)
	dim2 = len(s2)
	mindim = min(dim1, dim2)

	result = ""
	pos = 0
	while pos < mindim:
		result += s1[pos]
		if s1[pos] != s2[pos]:
			result += s2[pos]
		pos += 1

	# at most only one of the two following pieces of code will be executed
	while pos < dim1:
		result += s1[pos]
		pos += 1

	while pos < dim2:
		result += s2[pos]
		pos += 1
	return result
```

```python
def mergestrings_rec(s1, s2):
	if not s1: # s1 == "":
		return s2
	if not s2: # == "":
		return s1
	# general case
	res = s1[0]
	if s1[0] != s2[0]:
		res += s2[0]
	nexts1 = s1[1:]
	nexts2 = s2[1:]
	print(nexts1, nexts2)
	return res + mergestrings_rec(nexts1, nexts2)
```
:::


::: exefatti

Consider problem on translating from DNA to amino acid sequence: version with a csv file access

```python
import csv

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
            # creates a object, reader, able to read rows and extract its elements
            # based on the name of the column
            # avoids parsing and splitting 
            reader = csv.DictReader(infile)
            for row in reader:
                codon = row['Codon']
                one_letter = row['1Letter']
                codon_dic[codon] = one_letter
    except FileNotFoundError:
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
```

[file](../codice/90.dna2aa.filecsv.py)

:::

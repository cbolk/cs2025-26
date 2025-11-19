DICTNAME = "dictionary.en.txt"
ASCIICHARS_SIZE = 256   # number of existing ASCII characters

def find_anagrams(word, dicFilename):
    anagrams = []
    try:
        with open(dicFilename) as fin:
            # set up counter for the given word -- kept for the entire computation
            counters_w = [0] * ASCIICHARS_SIZE
            for c in word:
                counters_w[ord(c)] += 1
            # I will compare against it the counters I get for each dictionary word
            for line in fin:
                word_dic = line.strip().lower()
                if word != word_dic:
                    #in python is a single not expensive access
                    if len(word) == len(word_dic):
                        #I compute the counters for the dictionary word
                        counters_wd = [0] * ASCIICHARS_SIZE
                        for c in word_dic:
                            counters_wd[ord(c)] += 1
                            # can anticipate check ... is it sustainable/worth it?
                            if counters_wd[ord(c)] > counters_w[ord(c)]:
                                break
                        if counters_wd == counters_w:
                            anagrams.append(word_dic)

    except FileNotFoundError:
        print(f"Error: {dicFilename} not found.")
    except Exception as e:
        print("Error:", e)

    return anagrams

# ---- MAIN FLOW -----

word = input("Enter a word: ").strip().lower()
anagrams = find_anagrams(word, DICTNAME)

# Display results
for a in anagrams:
    print(a)
print(len(anagrams))


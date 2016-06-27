import sys

start = "<s>"
cxt = start
word = ""
freq = {}
bigrams = {}
eos = False

# Count bigrams

for line in sys.stdin:
    if line == "\n":
        word = "<e>"
        eos = True
    else:
        word = line.rstrip()
    if cxt not in bigrams:
        bigrams[cxt] = []
    if (cxt, word) not in freq:
        freq[(cxt, word)] = 0
        bigrams[cxt].append(word)        
    freq[(cxt,word)] += 1
    cxt = word
    if eos:
        cxt = start
        eos = False

# Print bigram frequencies

for c in sorted(bigrams.keys()):
    for w in sorted(bigrams[c]):
        print(c + "\t" + w + "\t" + str(freq[(c,w)]))

    
    

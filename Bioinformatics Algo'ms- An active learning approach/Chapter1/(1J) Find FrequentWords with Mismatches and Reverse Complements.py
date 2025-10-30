def reverseComp(string):
    comp = {'A':'T','T':'A','G':'C','C':'G'}
    return ''.join(comp[c] for c in reversed(string))

def symbolToNumber(symbol):
    return {'A':0,'C':1,'G':2,'T':3}[symbol]

def patternToNumber(pattern):
    if len(pattern) == 0:
        return 0
    return 4*patternToNumber(pattern[:-1]) + symbolToNumber(pattern[-1])

def numberToSymbol(num):
    return ['A','C','G','T'][num]

def numberToPattern(number, k):
    pattern = ''
    for _ in range(k):
        pattern = numberToSymbol(number % 4) + pattern
        number //= 4
    return pattern

def hamming_distance(s1, s2):
    return sum(ch1 != ch2 for ch1, ch2 in zip(s1, s2))

def neighbors(pattern, d):
    if d == 0:
        return {pattern}
    if len(pattern) == 1:
        return {'A','C','G','T'}
    
    neighborhood = set()
    suffix_neighbors = neighbors(pattern[1:], d)
    for text in suffix_neighbors:
        if hamming_distance(pattern[1:], text) < d:
            for nucleotide in ['A','C','G','T']:
                neighborhood.add(nucleotide + text)
        else:
            neighborhood.add(pattern[0] + text)
    return neighborhood

def frequentWordsWithMismatchesAndReverse(text, k, d):
    freqArray = [0]*(4**k)

    # Count for text
    for i in range(len(text)-k+1):
        for pattern in neighbors(text[i:i+k], d):
            freqArray[patternToNumber(pattern)] += 1

    # Count for reverse complement
    textRC = reverseComp(text)
    for i in range(len(textRC)-k+1):
        for pattern in neighbors(textRC[i:i+k], d):
            freqArray[patternToNumber(pattern)] += 1

    maxcount = max(freqArray)
    frequentPatterns = [numberToPattern(i, k) for i in range(4**k) if freqArray[i]==maxcount]

    return frequentPatterns

# --- Input ---
text = str(input("Enter DNA text: "))
k = int(input("Enter k-mer length: "))
d = int(input("Enter maximum mismatches (d): "))

frequent_patterns = frequentWordsWithMismatchesAndReverse(text, k, d)
print(*(frequent_patterns))

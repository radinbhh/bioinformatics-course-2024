def symbolToNumber(symbol):
    if symbol == 'A':
        return 0
    elif symbol == 'C':
        return 1
    elif symbol == 'G':
        return 2
    else:
        return 3

def patternToNumber(pattern):
    if len(pattern) == 0:
        return 0
    else:
        prefix = pattern[:-1]
        lastSymbol = pattern[-1]
        return 4 * patternToNumber(prefix) + symbolToNumber(lastSymbol)

def numberToSymbol(num):
    if num == 0:
        return 'A'
    elif num == 1:
        return 'C'
    elif num == 2:
        return 'G'
    else:
        return 'T'

def numberToPattern(number, k):
    pattern = ''
    for _ in range(k):
        remainder = number % 4
        pattern = numberToSymbol(remainder) + pattern
        number = number // 4
    return pattern

def hamming_distance(s1, s2):
    return sum(ch1 != ch2 for ch1, ch2 in zip(s1, s2))

def neighbors(pattern, d):
    if d == 0:
        return {pattern}
    if len(pattern) == 1:
        return {'A', 'C', 'G', 'T'}

    neighborhood = set()
    suffix_neighbors = neighbors(pattern[1:], d)
    for text in suffix_neighbors:
        if hamming_distance(pattern[1:], text) < d:
            for nucleotide in ['A', 'C', 'G', 'T']:
                neighborhood.add(nucleotide + text)
        else:
            neighborhood.add(pattern[0] + text)
    return neighborhood

def frequentWordsWithMismatches(text, k, d):
    frequencyArray = [0] * (4**k)

    for i in range(len(text) - k + 1):
        neighborhood = neighbors(text[i:i+k], d)
        for pattern in neighborhood:
            index = patternToNumber(pattern)
            frequencyArray[index] += 1

    maxcount = max(frequencyArray)
    frequentPatterns = []

    for i in range(4**k):
        if frequencyArray[i] == maxcount:
            frequentPatterns.append(numberToPattern(i, k))

    return frequentPatterns

# --- Input ---
text = str(input("Enter DNA text: "))
k = int(input("Enter k-mer length: "))
d = int(input("Enter maximum mismatches (d): "))

# --- Compute frequent patterns ---
frequent_patterns = frequentWordsWithMismatches(text, k, d)

print(*(frequent_patterns))

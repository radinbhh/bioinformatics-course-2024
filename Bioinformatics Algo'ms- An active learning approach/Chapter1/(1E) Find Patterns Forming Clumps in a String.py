def symbolToNumber(symbol):
    if symbol == 'A':
        return 0
    elif symbol == 'C':
        return 1
    elif symbol == 'G':
        return 2
    else:  # 'T'
        return 3

def patternToNumber(pattern):
    if len(pattern) == 0:
        return 0
    else:
        prefix = pattern[:-1]
        lastSymbol = pattern[-1]
        return 4 * patternToNumber(prefix) + symbolToNumber(lastSymbol)

def numberToPattern(number, k):
    mapping = {0: 'A', 1: 'C', 2: 'G', 3: 'T'}
    pattern = []
    for _ in range(k):
        number, remainder = divmod(number, 4)
        pattern.append(mapping[remainder])
    return ''.join(reversed(pattern))

def ComputingFrequencies(string, k):
    frequencyArray = [0] * (4 ** k)
    for i in range(len(string) - k + 1):
        pattern = string[i:i + k]
        frequencyArray[patternToNumber(pattern)] += 1
    return frequencyArray

def clumpFinding(genome, k, t, l):
    FrequentPatterns = []
    clump = [0] * (4 ** k)

    # Step 1: Compute frequencies in the first window
    text = genome[0:l]
    frequencyArray = ComputingFrequencies(text, k)

    for i in range(4**k):
        if frequencyArray[i] >= t:
            clump[i] = 1

    # Step 2: Slide the window across the genome
    for i in range(1, len(genome) - l + 1):
        firstPattern = genome[i - 1 : i - 1 + k]
        lastPattern = genome[i + l - k : i + l]

        frequencyArray[patternToNumber(firstPattern)] -= 1
        frequencyArray[patternToNumber(lastPattern)] += 1

        if frequencyArray[patternToNumber(lastPattern)] >= t:
            clump[patternToNumber(lastPattern)] = 1

    # Step 3: Collect all patterns forming clumps
    for i in range(4**k):
        if clump[i] == 1:
            FrequentPatterns.append(numberToPattern(i, k))

    return FrequentPatterns

# Example usage
genome = str(input("Enter genome: "))
k = int(input("Enter k: "))
l = int(input("Enter l: "))
t = int(input("Enter t: "))

result = clumpFinding(genome, k, t, l)
print(*result)

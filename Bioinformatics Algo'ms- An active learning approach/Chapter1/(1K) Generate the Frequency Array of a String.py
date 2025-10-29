def symbolToNumber(symbol):
    if (symbol == 'A'):
        return 0
    elif (symbol == 'C'):
        return 1
    elif (symbol == 'G'):
        return 2
    else:
        return 3

def patternToNumber(pattern):
    if (len(pattern) == 0):
        return 0
    else:
        prefix = pattern[0:len(pattern) - 1]
        lastSymbol = pattern[len(pattern) - 1]
        return 4 * patternToNumber(prefix) + symbolToNumber(lastSymbol)
    
def ComputingFrequencies(string , k):
    frequencyArray = []
    for i in range(4 ** k):
        frequencyArray.append(0)
    for i in range(len(string) - k + 1):
        pattern = string[i:i + k]
        frequencyArray[patternToNumber(pattern)] +=1
    return frequencyArray


pattern = str(input())
k = int(input())
print(*ComputingFrequencies(pattern, k))

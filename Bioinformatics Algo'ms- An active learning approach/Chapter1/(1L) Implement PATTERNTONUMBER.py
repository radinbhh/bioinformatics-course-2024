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
    

pattern = str(input())
print(patternToNumber(pattern))
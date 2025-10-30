def hamming_distance(s1, s2):
    if len(s1) != len(s2):
        raise ValueError("Strings must be of equal length")
    return sum(ch1 != ch2 for ch1, ch2 in zip(s1, s2))


def approximatePatternCount(string, pattern, k):
    count = []
    for i in range(len(string) - len(pattern) + 1):
        if (hamming_distance(string[i:i+len(pattern)], pattern) <= k):
            count.append(i)
    return count

pattern = str(input())
string = str(input())
k = int(input())
print(*(approximatePatternCount(string, pattern, k)))
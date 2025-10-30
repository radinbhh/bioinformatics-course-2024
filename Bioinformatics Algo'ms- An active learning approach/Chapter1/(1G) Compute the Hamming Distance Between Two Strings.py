def hamming_distance(s1, s2):
    if len(s1) != len(s2):
        raise ValueError("Strings must be of equal length")
    return sum(ch1 != ch2 for ch1, ch2 in zip(s1, s2))


string1 = str(input())
string2 = str(input())
print(hamming_distance(string1,string2))

def hamming_distance(s1, s2):
    if len(s1) != len(s2):
        raise ValueError("Strings must be of equal length")
    return sum(ch1 != ch2 for ch1, ch2 in zip(s1, s2))

def neighbors(pattern, d):
    if d == 0:
        return {pattern}
    if len(pattern) == 1:
        return {'A', 'C', 'T', 'G'}
    
    neighborhood = []
    suffix_neighbors = neighbors(pattern[1:], d)
    for text in suffix_neighbors:
        if hamming_distance(pattern[1:], text) < d:
            for nucleotide in ["A", "C", "G", "T"]:
                neighborhood.append(nucleotide + text)
        else:
            neighborhood.append(pattern[0] + text)
    
    return neighborhood

pattern = str(input("Enter the pattern: "))
k = int(input("Enter the number of mismatches (k): "))
neighborhood = neighbors(pattern, k)

# Write outputs to a file
with open("output.txt", "w") as f:
    for seq in neighborhood:
        f.write(seq + "\n")

print(f"All neighbors have been written to output.txt")

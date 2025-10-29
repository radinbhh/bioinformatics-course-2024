def pattern_count(string, pattern):
        count = 0
        for i in range(0, len(string) - len(pattern) + 1):
            if (string[i:i + len(pattern)] == pattern):
                count+=1

        return count


string = str(input())
pattern = str(input())
print(pattern_count(string,pattern))

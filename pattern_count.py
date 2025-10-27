def pattern_count(string, pattern):
        count = 0
        for i in range(0, len(string) - len(pattern)):
            if (string[i:i + len(pattern)] == pattern):
                count+=1

        return count


def frequent_words(string, k):
    frequent_patterns = []
    count = []
    max_count = -1
    for i in range(0,len(string) - k):
        pattern = string[i:i+k]
        count.append(pattern_count(string,pattern))
        if (count[i] > max_count):
           max_count = count[i]
    
    for i in range(0,len(string) - k):
        if (count[i] == max_count):
            frequent_patterns.append(string[i:i + k])
          
    frequent_patterns = list(set(frequent_patterns))
    return frequent_patterns
string = str(input("Enter the genome: "))
k = int(input("Enter k: "))
array = frequent_words(string,k)
for i in range(len(array)):
    print(array[i])

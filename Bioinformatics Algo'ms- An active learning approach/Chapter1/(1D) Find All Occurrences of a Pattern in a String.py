string = str(input())
pattern = str(input())
array = []
for i in range(0, len(string) - len(pattern) + 1):
    if (string[i:i+len(pattern)] == pattern):
        array.append(i)

print(array)
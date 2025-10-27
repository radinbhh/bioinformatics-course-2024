string = str(input())
string2 = ""
for i in range (len(string) - 1, -1, -1):
    if (string[i] == 'A'):
        string2 += 'T'
    elif (string[i] == 'T'):
        string2 += 'A'
    elif (string[i] == 'G'):
        string2 += 'C'
    else:
        string2 += 'G'
print(string2)
def numberToSymbol(num):
    if num == 0:
        return 'A'
    elif num == 1:
        return 'C'
    elif num == 2:
        return 'G'
    else:
        return 'T'

def numberToPattern(number, k):
    pattern = ''
    for _ in range(k):
        remainder = number % 4
        pattern = numberToSymbol(remainder) + pattern  # prepend to left
        number = number // 4
    return pattern

number = int(input("Enter number: "))
k = int(input("Enter k: "))
print(numberToPattern(number, k))

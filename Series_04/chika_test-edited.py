# read the number
original = number = int(input())
print(number)
result = ''

# loop to make provided operations
while number != 49 and number > 10:
    result = number[:-1] + number[-1] * 5
    print(result)
    # reassign the number
    number = result

# print depends on if the number is divisible by 7 ( iff 7 or 49)
print(f'{original} is { "not" if result == 7 or result == 49 else ""} divisible by 7')





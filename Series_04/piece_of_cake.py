num = input()

while num != '123':
    even, odd = 0, 0
    for digit in num:
        digit = int(digit)
        if digit % 2:
            odd += 1
        else:
            even += 1
    num = str(even) + str(odd) + str(even + odd)
    print(num)

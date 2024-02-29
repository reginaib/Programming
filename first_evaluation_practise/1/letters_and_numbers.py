inp = input().replace(' ', '')
total = 0
current = 0
sign = True
for char in inp:
    if char.isalpha():
        current += 1
    else:
        if sign:
            total += current
        else:
            total -= current
        sign = char == '+'
        current = 0

if sign:
    total += current
else:
    total -= current

print(total)

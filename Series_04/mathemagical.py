number = input()
length = len(number)

total = 0
for i in range(len(number)):
    term = int(number[:i] + number[i+1:])
    total += term
    print(f'{"+" if i == len(number) - 1 else " "} {term:{length}d}')

print('=' * (length + 1))
print(f'{total:{length+ 1}d}')

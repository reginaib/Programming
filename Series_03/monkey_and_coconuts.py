
pirates_num = int(input())
coconuts_num = int(input())

for p in range(1, pirates_num + 1):
    fraction, monkey = divmod(coconuts_num, pirates_num)
    if fraction == 1:
        s = 'nut'
    else:
        s = 'nuts'

    if monkey == 1:
        m = 'nut'
    else:
        m = 'nuts'

    print(f'{coconuts_num} nuts = {fraction} {s} for pirate#{p} and {monkey or "no"} {m} for the monkey')
    coconuts_num -= fraction + monkey

fraction, monkey = divmod(coconuts_num, pirates_num)

if fraction == 1:
    s = 'nut'
else:
    s = 'nuts'

if monkey == 1:
    m = 'nut'
else:
    m = 'nuts'

print(f'each pirate gets {fraction} {s} and {monkey or "no"} {m} for the monkey')

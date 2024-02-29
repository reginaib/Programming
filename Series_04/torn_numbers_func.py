def is_torn_number(num):
    for i in range(1, len(num)):
        part1 = int(num[:i])
        part2 = int(num[i:])
        if (part1 + part2)**2 == int(num):
            return True
    return False


num = input()

if is_torn_number(num):
    print('torn')
else:
    print('not torn')

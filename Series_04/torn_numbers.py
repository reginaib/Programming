num = input()

for i in range(1, len(num)):
    part1 = int(num[:i])
    part2 = int(num[i:])
    if (part1 + part2)**2 == int(num):
        print("torn")
        break
else:
    print("not torn")

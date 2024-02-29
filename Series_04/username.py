t = int(input())

for _ in range(t):
    full_name = input().lower()
    name, surname = full_name.split(' ')
    print(name[0] + surname[:4])

    if letter in puzzle.split('-')[int(n)]:
        print(n)
    elif letter in puzzle.split('-')[3:5]:
        print(1)
    elif letter in puzzle.split('-')[6:8]:
        print(2)
    elif letter in puzzle.split('-')[9:11]:
        print(3)
    else:
        print(-1)


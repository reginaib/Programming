n = int(input())
first_word = input()
first_lower = first_word.lower()

if first_lower[0] != first_lower[-1]:
    print(first_word)
else:
    for _ in range(1, n):
        second_word = input()
        second_lower = second_word.lower()

        if second_lower[0] != second_lower[-1]:
            print(second_word)
            break
        elif (ord(first_lower[-1]) - ord('a') + 1) % 26 != ord(second_lower[0]) - ord('a'):
            print(second_word)
            break
        first_word = second_word
        first_lower = second_lower
    else:
        print('no mistake')

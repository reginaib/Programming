word = input()
start = input()
abc = 'abcdefghijklmnopqrstuvwxyz' * 2

i1 = abc.index(word[0].lower())
i2 = abc.index(start.lower(), i1)
diff = i2 - i1

print(word[0] + abc[i1 + 1:i2] + start)
for char in word[1:]:
    i1 = abc.index(char.lower())
    i2 = i1 + diff
    print(char + abc[i1 + 1: i2] + abc[i2].upper())

word1 = input()
word2 = input()

prefix = ''

for char1, char2 in zip(word1, word2):
    if char1 == char2:
        prefix += char1
    else:
        break

suffix = ''

for char1, char2 in zip(reversed(word1), reversed(word2)):
    if char1 == char2:
        suffix = char1 + suffix
    else:
        break

lp = len(prefix)
ls = len(suffix)
max_len = max(len(word1), len(word2))

print(' ' * lp + f'┏{word1[lp:len(word1) - ls]:^{max_len - lp - ls}}┓')
print(prefix + '┫' + ' ' * (max_len - ls - lp) + '┣' + suffix)
print(' ' * lp + f'┗{word2[lp:len(word2) - ls]:^{max_len - lp - ls}}┛')

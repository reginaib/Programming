top_line = input()
bottom_line = input()

notation_to_letter = {
        '****': 'C',
        '*o**': 'D',
        '***o': 'E',
        '*o*o': 'F',
        'oo**': 'G',
        'oo*o': 'A',
        'o*oo': 'B',
        'oooo': 'C'
    }

if (len(top_line) != len(bottom_line)
        or len(top_line) % 2
        or top_line.replace('o', '').replace('*', '')
        or bottom_line.replace('o', '').replace('*', '')):
    result = 'MYSTERY GUEST'
else:
    result = ''
    for i in range(0, len(top_line), 2):
        key = top_line[i:i+2] + bottom_line[i:i+2]
        result += notation_to_letter.get(key, '?')
print(result)

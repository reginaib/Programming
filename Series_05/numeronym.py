def numeronym(word):
    if len(word) < 4:
        return word
    return f'{word[0]}{len(word)-2}{word[-1]}'


def template(word):
    output = ''
    digits = ''

    for char in word:
        if char.isdigit():
            digits += char
        else:
            if digits:
                output += '.' * int(digits)
                digits = ''
            output += char
    if digits:
        output += '.' * int(digits)
    return output


def isnumeronym(word1, word2):
    word1 = template(word1)

    if len(word1) != len(word2):
        return False

    for char1, char2 in zip(word1.lower(), word2.lower()):
        if char1 != '.' and char1 != char2:
            return False
    return True

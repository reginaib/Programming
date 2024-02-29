def character_value(char):
    char = char.upper()
    if 'A' <= char <= 'Z':
        return ord(char) - ord('A') + 1
    return 0


def string_value(s):
    s = s.upper()
    value = 0
    for char in s:
        value += character_value(char)
    return value


def istantamount(str1, str2):
    return string_value(str1) == string_value(str2)


def isequality(equation):
    if '=' in equation and equation.count('=') == 1:
        left, right = equation.split('=')
        return istantamount(left.strip(), right.strip())
    return False


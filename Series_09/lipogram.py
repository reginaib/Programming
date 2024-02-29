# https://dodona.be/nl/courses/2802/series/29675/activities/1815535490

def occurrences(file_name):
    """
    >>> occurrences('lipo.txt')
    {'i': 21, 'm': 5, 't': 22, 'h': 8, 'n': 16, 'k': 3, 'g': 4, 'o': 12, 'f': 2, 'a': 19, 'r': 7, 'l': 6, 'q': 1, 'u': 9, 'y': 3, 'p': 1, 'c': 4, 's': 8, 'd': 6, 'w': 4, 'b': 2}
    """
    result = {}
    with open(file_name, 'r', encoding='utf8') as file:
        for char in file.read().lower():
            if char in result:
                result[char] += 1
            elif char.isalpha():
                result[char] = 1
    return result


def missing_letters(file_name):
    """
    >>> missing_letters('lipo.txt')
    {'e', 'j', 'v', 'x', 'z'}
    """
    return set('abcdefghijklmnopqrstuvwxyz') - occurrences(file_name).keys()


def make_lipogram(to_remove, file_name, output=None):
    result = []
    with open(file_name, 'r', encoding='utf-8') as file:
        for line in file:
            for x in to_remove:
                line = line.replace(x.lower(), '')
            for x in to_remove:
                line = line.replace(x.upper(), '')
            result.append(line)

    if output is None:
        print(''.join(result), end='')
    else:
        with open(output, 'w', encoding='utf8') as file:
            file.writelines(result)

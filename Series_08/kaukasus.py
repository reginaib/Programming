# https://dodona.be/nl/courses/2802/series/29674/activities/1439343716
def occurrences(word):
    """
    >>> occurrences('Caucasus') ==  {'a': 2, 'c': 2, 'u': 2, 's': 2}
    True
    >>> occurrences('teammate') == {'a': 2, 'm': 2, 'e': 2, 't': 2}
    True
    >>> occurrences('SCINTILLESCENT') == {'c': 2, 'e': 2, 'i': 2, 'l': 2, 'n': 2, 's': 2, 't': 2}
    True
    >>> occurrences('chachacha') == {'a': 3, 'h': 3, 'c': 3}
    True
    >>> occurrences('blahblahblahblah') ==  {'a': 4, 'h': 4, 'b': 4, 'l': 4}
    True
    >>> occurrences('intestine') == {'i': 2, 's': 1, 'e': 2, 't': 2, 'n': 2}
    True
    """
    number_of_occurrences = {}
    for letter in word.lower():
        if letter in number_of_occurrences:
            number_of_occurrences[letter] += 1
        else:
            number_of_occurrences[letter] = 1
    return number_of_occurrences


def balanced(word):
    """
    >>> balanced('Caucasus')
    True
    >>> balanced('teammate')
    True
    >>> balanced('SCINTILLESCENT')
    True
    >>> balanced('lysosome')
    False
    >>> balanced('intestines')
    True
    >>> balanced('mesosome')
    True
    """
    item = None
    for key, value in occurrences(word).items():
        if value < 2:
            return False
        elif item is None:
            item = value
        elif item != value:
            return False
    return True


if __name__ == '__main__':
    import doctest
    doctest.testmod()

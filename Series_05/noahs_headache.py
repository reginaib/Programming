def split(species):

    """
    Splits the parameter (str) in a prefix and a suffix, where the prefix is
    formed by the longest sequence of consonants at the start of the parameter.

    >>> split('sheep')
    ('sh', 'eep')
    >>> split('goat')
    ('g', 'oat')
    """
    prefix = ''

    for char in species:
        if char.lower() not in ('a', 'e', 'i', 'o', 'u'):
            prefix += char
        else:
            break
    suffix = species[len(prefix):]
    return prefix, suffix


def hybridize(species1, species2):

    """
    Returns a tuple containing two strings. The first element of the tuple is
    formed by concatenating the prefix of the first parameter and the suffix
    of the second parameter. The second element of the tuple is formed by
    concatenating the prefix of the second parameter and the suffix of the
    first parameter.

    >>> hybridize('sheep', 'goat')
    ('shoat', 'geep')
    >>> hybridize('lion', 'tiger')
    ('jeopard', 'laguar')
    >>> hybridize('schnauzer', 'poodle')
    ('schnoodle', 'pauzer')
    """
    prefix1, suffix1 = split(species1)
    prefix2, suffix2 = split(species2)
    return prefix1 + suffix2, prefix2 + suffix1


if __name__ == '__main__':
    import doctest
    doctest.testmod()

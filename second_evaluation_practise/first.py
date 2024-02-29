

def isspellable(word1, word2: str):
    """
    >>> isspellable('houseplant', 'oesHpln')
    False
    >>> isspellable('phone', 'oesHpln')
    True
    >>> isspellable('epsilon', 'oesHpln')
    False
    >>> isspellable('loophole', 'oesHpln')
    True
    >>> isspellable('OPENS', 'OESHpLN')
    True
    """
    return set(word1.lower()).issubset(word2.lower())


def ispangram(word1, word2):
    """
    >>> ispangram('helplessness', 'oesHpln')
    False
    >>> ispangram('hopelessness', 'oesHpln')
    True
    """
    return set(word1.lower()) == set(word2.lower())


def solutions(location, puzzle, minimum=4):
    """
    >>> solutions('words.txt', 'oesHpln')
    {'hones', 'hellos', 'hopelessness', 'shone', 'hopes', 'shoon', 'hellholes', 'heels', 'nosh', 'shoos', 'hello', 'hoop', 'hell', 'loopholes', 'shells', 'hoes', 'loophole', 'noshes', 'hopeless', 'phones', 'sloshes', 'hens', 'shes', 'helplessness', 'holes', 'shell', 'hops', 'peepholes', 'hose', 'pooh', 'hope', 'posh', 'phone', 'hellhole', 'shleps', 'shlepps', 'shoe', 'shlep', 'shops', 'poohs', 'shop', 'shoes', 'slosh', 'sheep', 'hole', 'helpless', 'hoops', 'helps', 'hoses', 'help', 'shlepp', 'shoo', 'hone', 'peephole', 'sheen', 'heel'}
    >>> solutions('words.txt', 'oesHpln', minimum=10)
    {'hopelessness', 'helplessness'}
    >>> solutions('words.txt', 'ocgrNminas')     # two occurrences of letter N
    Traceback (most recent call last):
    AssertionError: invalid puzzle
    >>> solutions('words.txt', 'LpuomsietrgnC')  # two capitals
    Traceback (most recent call last):
    AssertionError: invalid puzzle
    """
    assert len(puzzle) > 1, 'invalid puzzle'
    assert len(set(puzzle.lower())) == len(puzzle), 'invalid puzzle'
    assert sum(c.isupper() for c in puzzle) == 1, 'invalid puzzle'

    result = set()
    with open(location, encoding='utf8') as f:
        for w in f:
            w = w.strip()
            if len(w) >= minimum and isspellable(w, puzzle) and {c.lower() for c in puzzle
                                                                 if c.isupper()}.issubset(w.lower()):
                result.add(w)
    return result


def pangrams(location, puzzle):
    """
    >>> pangrams('words.txt', 'oesHpln')
    {'hopelessness'}
    >>> pangrams('words.txt', 'ocgrNmias')
    {'microorganism', 'microorganisms'}
    >>> pangrams('words.txt', 'Lpuomsietrgnc')
    {'multiprocessing'}
    """
    assert len(puzzle) > 1, 'invalid puzzle'
    assert len(set(puzzle.lower())) == len(puzzle), 'invalid puzzle'
    assert sum(c.isupper() for c in puzzle) == 1, 'invalid puzzle'

    result = set()
    with open(location, encoding='utf8') as f:
        for w in f:
            w = w.strip()
            if ispangram(w, puzzle):
                result.add(w)
    return result


if __name__ == '__main__':
    import doctest
    doctest.testmod()

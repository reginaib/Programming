from itertools import islice, zip_longest


def group(pile, n):
    '''
    >>> cards = ['KS', '4H', 'KH', 'JD', '10S', '2D', '9C', 'JH']
    >>> group(cards, 2)
    [('KS', '4H'), ('KH', 'JD'), ('10S', '2D'), ('9C', 'JH')]
    >>> group(cards, 4)
    [('KS', '4H', 'KH', 'JD'), ('10S', '2D', '9C', 'JH')]
    >>> group(cards, 3)
    Traceback (most recent call last):
    AssertionError: invalid grouping
    >>> group(cards, [2, 4, 2])
    [('KS', '4H'), ('KH', 'JD', '10S', '2D'), ('9C', 'JH')]
    >>> group(cards, (3, 2, 3))
    [('KS', '4H', 'KH'), ('JD', '10S'), ('2D', '9C', 'JH')]
    >>> group(cards, [3, 1, 3])
    Traceback (most recent call last):
    AssertionError: invalid grouping
    '''
    iterator = iter(pile)
    result = []
    if isinstance(n, int):
        assert n > 0, 'invalid grouping'
        while gr := tuple(islice(iterator, n)):
            assert len(gr) == n, 'invalid grouping'
            result.append(gr)
    else:
        assert isinstance(n, (list, tuple)) and all(isinstance(i, int) for i in n), 'invalid grouping'
        for i in n:
            assert i > 0, 'invalid grouping'
            gr = tuple(islice(iterator, i))
            assert len(gr) == i, 'invalid grouping'
            result.append(gr)
        assert next(iterator, None) is None, 'invalid grouping'
    return result


def riffle_shuffle(pile1, pile2):
    '''
    >>> pile1 = [('7C', '2D', 'JC'), ('7H', '10S', '9D'), ('5C', 'AH', '3C')]
    >>> pile2 = [('AD', '9C'), ('KD', '10C', 'QH', 'JS'), ('4D', 'AS', '8D')]
    >>> pile3 = [('AD',), ('9C', 'KD', '10C'), ('QH', 'JS'), ('4D', 'AS', '8D')]
    >>> riffle_shuffle(pile1, pile2)
    ['7C', '2D', 'JC', 'AD', '9C', '7H', '10S', '9D', 'KD', '10C', 'QH', 'JS', '5C', 'AH', '3C', '4D', 'AS', '8D']
    >>> riffle_shuffle(pile1, pile3)
    Traceback (most recent call last):
    AssertionError: different number of groups
    '''
    result = []
    for gr1, gr2 in zip_longest(pile1, pile2):
        assert gr1 is not None and gr2 is not None, 'different number of groups'
        result.extend(gr1)
        result.extend(gr2)
    return result


def mixed_pairs(pile):
    """
    >>> pile1 = [('7C', '2D', 'JC'), ('7H', '10S', '9D'), ('5C', 'AH', '3C')]
    >>> pile2 = [('AD', '9C'), ('KD', '10C', 'QH', 'JS'), ('4D', 'AS', '8D')]
    >>> new_pile = riffle_shuffle(pile1, pile2)
    >>> mixed_pairs(new_pile)
    True
    >>> mixed_pairs(['7C', '2D', 'JC', '7H', '10S', '9D', '5C', 'AH', '3C'])
    Traceback (most recent call last):
    AssertionError: odd number of cards
    """
    assert len(pile) % 2 == 0, 'odd number of cards'
    for card1, card2 in group(pile, 2):
        if card1.endswith(('S', 'C')):
            if not card2.endswith(('D', 'H')):
                return False
        elif card1.endswith(('D', 'H')):
            if not card2.endswith(('S', 'C')):
                return False
    return True


if __name__ == '__main__':
    import doctest
    doctest.testmod()





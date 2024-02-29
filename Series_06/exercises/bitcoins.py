# https://dodona.be/nl/courses/2802/series/29672/activities/284336818
def profit(rates, actions):
    """
    >>> profit([5, 11, 4, 2, 8, 10, 7, 4, 3, 6], 'BS-B-S--BS')
    17
    >>> profit((4, 2, 5, 11, 10, 4, 11, 7, 4, 11, 3, 11), '-B-S-BS-BSBS')
    31
    >>> profit([10, 9, 9, 10, 10, 9, 1, 4, 9, 3, 5, 6, 10], '-B-S--B-SB--S')
    16
    >>> profit((12, 4, 9, 5, 6, 7, 9, 9, 11, 7, 10), '-BSB----SBS')
    14
    >>> profit([10, 9, 8, 7, 6, 5, 4, 3, 2, 1], '----------')
    0
    >>> profit((10, 4, 2, 4, 8, 12), 'B---SS')
    Traceback (most recent call last):
    AssertionError: invalid actions
    """
    assert isinstance(actions, str), 'invalid actions'
    assert len(actions) == len(rates), 'invalid actions'

    total = 0
    bitcoin = False
    for r, a in zip(rates, actions):
        if a == 'B':
            assert not bitcoin, 'invalid actions'
            bitcoin = True
            total -= r
        elif a == 'S':
            assert bitcoin,'invalid actions'
            bitcoin = False
            total += r
        else:
            assert a == '-', 'invalid actions'

    assert a != 'B', 'invalid actions'
    if bitcoin:
        total += r
    return total


def maximal_profit(rates):
    """
    >>> maximal_profit([5, 11, 4, 2, 8, 10, 7, 4, 3, 6])
    17
    >>> maximal_profit((4, 2, 5, 11, 10, 4, 11, 7, 4, 11, 3, 11))
    31
    >>> maximal_profit([10, 9, 9, 10, 10, 9, 1, 4, 9, 3, 5, 6, 10])
    16
    >>> maximal_profit((12, 4, 9, 5, 6, 7, 9, 9, 11, 7, 10))
    14
    >>> maximal_profit([10, 9, 8, 7, 6, 5, 4, 3, 2, 1])
    0
    >>> maximal_profit((10, 4, 2, 4, 8, 12))
    10
    """
    bitcoin = False
    total = 0
    for today, tomorrow in zip(rates, rates[1:]):
        if bitcoin:
            if today > tomorrow:
                bitcoin = False
                total += today
        elif tomorrow > today:
            bitcoin = True
            total -= today
    if bitcoin:
        total += tomorrow
    return total


def optimal_actions(rates):
    """
    >>> optimal_actions([5, 11, 4, 2, 8, 10, 7, 4, 3, 6])
    'BS-B-S--BS'
    >>> optimal_actions((4, 2, 5, 11, 10, 4, 11, 7, 4, 11, 3, 11))
    '-B-S-BS-BSBS'
    >>> optimal_actions([10, 9, 9, 10, 10, 9, 1, 4, 9, 3, 5, 6, 10])
    '--B-S-B-SB--S'
    >>> optimal_actions((12, 4, 9, 5, 6, 7, 9, 9, 11, 7, 10))
    '-BSB----SBS'
    >>> optimal_actions([10, 9, 8, 7, 6, 5, 4, 3, 2, 1])
    '----------'
    >>> optimal_actions((10, 4, 2, 4, 8, 12))
    '--B--S'
    """
    bitcoin = False
    actions = ''
    for today, tomorrow in zip(rates, rates[1:]):
        if bitcoin:
            if today > tomorrow:
                bitcoin = False
                actions += 'S'
            else:
                actions += '-'
        elif tomorrow > today:
            bitcoin = True
            actions += 'B'
        else:
            actions += '-'
    if bitcoin:
        actions += 'S'
    else:
        actions += '-'
    return actions


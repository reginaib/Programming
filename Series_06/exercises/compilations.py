def divide(comp):
    """
    >>> divide('WOODSman')
    ('WOODS', 'man')
    >>> divide('billION')
    ('bill', 'ION')
    """

    first, second = '', ''
    flag = comp[0].isupper()

    for char in comp:
        if char.isupper() == flag:
            first += char
        else:
            second += char
    return first, second


def recombine(seq):
    '''
    >>> recombine(['WOODSman', 'AGEing', 'RAINbow', 'MENtal', 'LOWdown', 'PLAYback'])
    ['manAGE', 'ingRAIN', 'bowMEN', 'talLOW', 'downPLAY', 'backWOODS']
    >>> recombine(('billION', 'isingLASS', 'oedEMA', 'nationWIDE', 'screenPLAY'))
    ['IONising', 'LASSoed', 'EMAnation', 'WIDEscreen', 'PLAYbill']
    '''
    # result = []
    # for i in range(len(seq)):
    #     current_c = divide(seq[i])
    #     next_c = divide(seq[(i + 1) % len(seq)])
    #
    #     word = current_c[1] + next_c[0]
    #     result.append(word)
    # return result

    result = []
    prefix, suffix = divide(seq[0])
    for word in seq[1:]:
        first, second = divide(word)
        result.append(suffix + first)
        suffix = second
    result.append(suffix + prefix)
    return result


def successors(comp, seq):
    '''
    >>> successors('WOODSman', ['backWOODS', 'manAGE', 'LOWdown', 'ingRAIN', 'AGEing', 'talLOW', 'MENtal', 'bowMEN', 'RAINbow', 'downPLAY', 'PLAYback', 'WOODSman'])
    ['manAGE']
    >>> successors('boardWALK', ('nationWIDE', 'PLAYbill', 'EMAnation', 'IONising', 'isingLASS', 'WIDEscreen', 'oedEMA', 'billION', 'LASSoed', 'screenPLAY'))
    []
    >>> successors('rocketMAN', ['manGROVE', 'roMANTIC', 'MANUscript', 'MANkind', 'HUman', 'MANtra', 'KLEPTOmania'])
    ['manGROVE', 'MANkind', 'MANtra']
    '''
    result = []
    suffix = divide(comp)[1].lower()

    for word in seq:
        prefix = divide(word)[0]
        if suffix == prefix.lower():
            result.append(word)
    return result


def intertwine(seq):
    '''
    >>> intertwine(['backWOODS', 'manAGE', 'LOWdown', 'ingRAIN', 'AGEing', 'talLOW', 'MENtal', 'bowMEN', 'RAINbow', 'downPLAY', 'PLAYback', 'WOODSman'])
    (['AGEing', 'RAINbow', 'MENtal', 'LOWdown', 'PLAYback', 'WOODSman'], ['ingRAIN', 'bowMEN', 'talLOW', 'downPLAY', 'backWOODS', 'manAGE'])
    >>> intertwine(('nationWIDE', 'PLAYbill', 'EMAnation', 'IONising', 'isingLASS', 'WIDEscreen', 'oedEMA', 'billION', 'LASSoed', 'screenPLAY'))
    (['billION', 'isingLASS', 'oedEMA', 'nationWIDE', 'screenPLAY'], ['IONising', 'LASSoed', 'EMAnation', 'WIDEscreen', 'PLAYbill'])
    '''
    # making a copy of a list to avoid data corruption
    seq_copy = list(seq)
    current_word = min(seq_copy, key=lambda x: x.lower())  # key determines the order of the comparison
    seq_copy.remove(current_word)

    first, second = [], []
    first.append(current_word)
    current_list = second
    next_list = first

    for _ in range(len(seq_copy)):
        successor = successors(current_word, seq_copy)
        assert successor, 'invalid sequence'
        # taking the first element
        current_word = successor[0]
        current_list.append(current_word)
        seq_copy.remove(current_word)
        # switch the lists
        current_list, next_list = next_list, current_list
    return first, second


if __name__ == '__main__':
    import doctest
    doctest.testmod()


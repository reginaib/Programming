def average(seq):
    '''
    >>> average((5, 6, 7, 8, 9))
    7.0
    >>> average([1, 2, 3, 4])
    2.5
    '''
    return sum(seq)/len(seq)


def move1(seq1, seq2, seq3):
    '''
    >>> seq1 = [5, 6, 7, 8, 9]
    >>> seq2 = [1, 2, 3, 4]
    >>> seq3 = [5]
    >>> move1(seq1, seq2, seq3)
    >>> seq1
    [6, 7, 8, 9]
    >>> seq2
    [1, 2, 3, 4, 5]
    >>> seq3
    [5]
    '''
    for i in seq3:
        if i in seq1:
            seq1.remove(i)
            seq2.append(i)


def move2(seq1, seq2, seq3):
    '''
    >>> seq1 = (5, 6, 7, 8, 9)
    >>> seq2 = [1, 2, 3, 4]
    >>> seq3 = [5]
    >>> move2(seq1, seq2, seq3)
    ([6, 7, 8, 9], [1, 2, 3, 4, 5])
    >>> seq1
    (5, 6, 7, 8, 9)
    >>> seq2
    [1, 2, 3, 4]
    >>> seq3
    [5]
    '''
    seq1_mut = list(seq1)
    seq2_mut = list(seq2)
    move1(seq1_mut, seq2_mut, seq3)
    return seq1_mut, seq2_mut


def iswillrogers(seq1, seq2, seq3):
    '''
    >>> iswillrogers([5, 6, 7, 8, 9], [1, 2, 3, 4], [5])
    True
    >>> iswillrogers((5, 6, 7, 8, 9), (1, 2, 3, 4), (7, 9))
    False
    '''
    seq4, seq5 = move2(seq1, seq2, seq3)
    return average(seq4) > average(seq1) and average(seq5) > average(seq2)


if __name__ == '__main__':
    import doctest
    doctest.testmod()

def product(integers, positions=None):
    """
    >>> product([2, 3, 11, 23, 31])
    47058
    >>> product((2, 3, 7, 47, 395), [0])
    389865
    >>> product([2, 3, 7, 47, 583, 1223], (1, 3))
    9982126
    >>> product((2, 3, 7, 43, 3263, 4051, 2558951), (0, 2, 4))
    1337254054629
    """
    if positions is not None:
        integers = list(integers)
        for j in sorted(positions, reverse=True):
            del integers[j]

    result = 1
    for i in integers:
        result *= i
    return result

    # def product(integers, positions=None):
    #     if positions is None:
    #         positions = []
    #     result = 1
    #     for i in range(len(integers)):
    #         if i not in positions:
    #             result *= integers[i]
    #     return result


def transform(numbers, position):
    """
    >>> transform([2, 3, 11, 23, 31], 0)
    11765
    >>> transform((2, 3, 11, 23, 31), 1)
    5229
    >>> transform([2, 3, 11, 23, 31], 2)
    389
    >>> transform((2, 3, 11, 23, 31), 3)
    89
    >>> transform([2, 3, 11, 23, 31], 4)
    49
    >>> transform((2, 3, 4, 5, 6), 3)
    29
    >>> transform((2, 3, 4, 5, 6), 4)
    Traceback (most recent call last):
    AssertionError: invalid transformation
    """
    td1, td2 = divmod((product(numbers, positions=[position]) + 1), numbers[position])
    assert td2 == 0, 'invalid transformation'
    return td1


def transformation(numbers):
    """
    >>> transformation([2, 3, 11, 23, 31])
    [11765, 5229, 389, 89, 49]
    >>> transformation((2, 3, 7, 47, 395))
    [194933, 86637, 15913, 353, 5]
    >>> transformation([2, 3, 7, 47, 583, 1223])
    [351869942, 156386641, 28724077, 637157, 4141, 941]
    >>> transformation((2, 3, 7, 43, 3263, 4051, 2558951))
    [15272109930890495, 6787604413729109, 1246702851501265, 33038636951629, 5737528889, 3722498629, 9329]
    >>> transformation([2, 3, 11, 25, 29, 1097, 2753])
    [36127240463, 16056551317, 1194288941, 231214339, 171829919, 120083, 19067]
    >>> transformation((2, 3, 4, 5, 6))
    Traceback (most recent call last):
    AssertionError: invalid transformation
    """
    result = []
    for i in range(len(numbers)):
        number = transform(numbers, i)
        result.append(number)
    return result


def ink_cognito(seq1, seq2):
    """
    >>> ink_cognito([2, 3, 7, 47, None], [194933, None, None, 353, 5])
    ([2, 3, 7, 47, 395], [194933, 86637, 15913, 353, 5])
    >>> ink_cognito((2, 3, 11, None, 31), (None, 5229, 389, None, 49))
    ([2, 3, 11, 23, 31], [11765, 5229, 389, 89, 49])
    >>> ink_cognito([2, 3, 7, 47, 583, None], [None, None, None, None, None, 941])
    ([2, 3, 7, 47, 583, 1223], [351869942, 156386641, 28724077, 637157, 4141, 941])
    """
    complete_seq1 = list(seq1)
    complete_seq2 = list(seq2)

    seq1_n_ind = seq1.index(None)
    seq2_n_ind = seq2[seq1_n_ind]

    if seq2_n_ind is not None:
        obs_num = (product(seq1, [seq1_n_ind]) + 1) // seq2_n_ind
        complete_seq1[seq1_n_ind] = obs_num
        complete_seq2 = transformation(complete_seq1)
    else:
        obs_num = (seq1[seq1_n_ind - 1] * seq2[seq1_n_ind - 1] - 1) // product(seq1, seq1[:seq1_n_ind - 1])
        complete_seq1[seq1_n_ind] = obs_num
        complete_seq2 = transformation(complete_seq1)

    return complete_seq1, complete_seq2


if __name__ == '__main__':
    import doctest
    doctest.testmod()

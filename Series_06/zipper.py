from itertools import cycle


def merge(seq1, seq2):
    """
    >>> merge(('A', 'B', 'C'),  [1, 2, 3])
    ['A', 1, 'B', 2, 'C', 3]
    >>> merge(['A'], [1, 2, 3, 4])
    ['A', 1]
    >>> merge(('A', 'B'),  (1, 2, 3, 4))
    ['A', 1, 'B', 2]
    >>> merge(('A', 'B', 'C'),  [1, 2])
    ['A', 1, 'B', 2]
    """
    merge_list = []

    for elem1, elem2 in zip(seq1, seq2):
        merge_list.append(elem1)
        merge_list.append(elem2)

    return merge_list


def weave(seq1, seq2):
    """
    >>> weave(('A', 'B', 'C'),  [1, 2, 3])
    ['A', 1, 'B', 2, 'C', 3]
    >>> weave(['A'], [1, 2, 3, 4])
    ['A', 1, 'A', 2, 'A', 3, 'A', 4]
    >>> weave(('A', 'B'),  (1, 2, 3, 4))
    ['A', 1, 'B', 2, 'A', 3, 'B', 4]
    >>> weave(('A', 'B', 'C'),  [1, 2])
    ['A', 1, 'B', 2, 'C', 1]
    """
    merge_list = []
    len1, len2 = len(seq1), len(seq2)
    max_len = max(len1, len2)
    seq1_cycle, seq2_cycle = cycle(seq1), cycle(seq2)

    for i in range(max_len):
        merge_list.append(next(seq1_cycle))
        merge_list.append(next(seq2_cycle))
    return merge_list




def zipper(seq1, seq2):
    """
    >>> zipper(('A', 'B', 'C'),  [1, 2, 3])
    ['A', 1, 'B', 2, 'C', 3]
    >>> zipper(['A'], [1, 2, 3, 4])
    ['A', 1, 2, 3, 4]
    >>> zipper(('A', 'B'),  (1, 2, 3, 4))
    ['A', 1, 'B', 2, 3, 4]
    >>> zipper(('A', 'B', 'C'),  [1, 2])
    ['A', 1, 'B', 2, 'C']
    """
    merged = merge(seq1, seq2)

    len1, len2 = len(seq1), len(seq2)
    if len1 > len2:
        merged.extend(seq1[len2:])
    elif len2 > len1:
        merged.extend(seq2[len1:])

    return merged


if __name__ == '__main__':
    import doctest
    doctest.testmod()
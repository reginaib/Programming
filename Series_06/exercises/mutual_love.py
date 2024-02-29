def positions(word):
    '''
    >>> positions('LOVE')
    (11, 14, 21, 4)
    >>> positions('mutual')
    (12, 20, 19, 20, 0, 11)
    '''
    char_ids = []
    for char in word.lower():
        char_ids.append(ord(char) - ord('a'))
    return tuple(char_ids)

    # return tuple(ord(char) - ord('a') for char in word.lower())


def ismutual(seq, num):
    '''
    >>> ismutual((11, 14, 21, 4), 26)
    True
    >>> ismutual([12, 20, 19, 20, 0, 11], 26)
    False
    '''
    seq_sorted = sorted(seq)

    for i in range(len(seq) // 2):
        if seq_sorted[i] + seq_sorted[-i - 1] != num - 1:
            return False
    return True


def mutual_love(word):
    '''
    >>> mutual_love('LOVE')
    True
    >>> mutual_love('mutual')
    False
    '''
    word_pos = positions(word)
    num = min(word_pos) + max(word_pos) + 1
    #word_sorted = sorted(positions(word)) it is more demanding computationally
    #num = word_sorted[0] + word_sorted[-1] + 1
    return ismutual(word_pos, num)


if __name__ == '__main__':
    import doctest
    doctest.testmod()

def valid_solution(integers, side=None):

    """
    >>> valid_solution([1, 6, 12, 2, 5, 11, 3, 9, 7, 4, 8, 10])
    True
    >>> valid_solution([1, 6, 12, 2, 5, 11, 3, 9, 7, 4, 8, 10], side=19)
    True
    >>> valid_solution([1, 6, 12, 2, 5, 11, 3, 9, 7, 4, 8, 10], side=20)
    False
    >>> valid_solution([1, 7, 12, 3, 5, 9, 6, 4, 10, 2, 8, 11], side=20)
    True
    >>> valid_solution([4, 3, 5, 1, 6, 2])
    True
    >>> valid_solution([5, 2, 6, 3, 4, 8, 1, 7], 13)
    True
    >>> valid_solution([7, 8, 1, 10, 5, 2, 9, 4, 3, 6], 16)
    True
    """

    # check whether the number of integers in the given list is even and greater
    # then or equal to six
    n = len(integers)
    if n % 2 or n < 6:
        return False

    # check whether each integer between 1 and n occurs exactly once in the
    # given list of integers
    for i in range(n):
        if i + 1 not in integers:
            return False

    # determine sum of the last side
    last_side = integers[0] + integers[-1] + integers[-2]

    # check whether sum of the last side equals the given sum
    if side is not None and side != last_side:
        return False

    # check whether each side has an equal sum of its numbers
    for i in range(0, n - 2, 2):
        if last_side != sum(integers[i:i + 3]):
            return False

    # all conditions are fulfilled: the solution is correct
    return True

if __name__ == '__main__':
    import doctest
    doctest.testmod()

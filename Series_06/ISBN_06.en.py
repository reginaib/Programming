def isISBN(code):

    """
    Checks if the given ISBN-10 code is valid.

    >>> isISBN('9-9715-0210-0')
    True
    >>> isISBN('997-150-210-0')
    False
    >>> isISBN('9-9715-0210-8')
    False
    """

    # check if the given code is a string
    if not isinstance(code, str):
        return False

    # check if dashes are at the correct positions and if each group has the correct number of digits
    groups = code.split('-')
    if [len(e) for e in groups] != [1, 4, 4, 1]:
        return False

    # remove dashes from the given code
    code = ''.join(groups)

    # check if all characters (except the final one) are digits
    if not code[:-1].isdigit():
        return False

    # check the check digit of the given code
    return checkdigit(code) == code[-1]


def checkdigit(code):

    """
    >>> checkdigit('997150210')
    '0'
    >>> checkdigit('938389293')
    '5'
    """

    # compute check digit
    check = sum(index * int(digit) for index, digit in enumerate(code[:9], start=1)) % 11

    # convert check digit into its string representation
    return 'X' if check == 10 else str(check)


if __name__ == '__main__':
    import doctest
    doctest.testmod()

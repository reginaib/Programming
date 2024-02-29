def isISBN(code):

    """
    Returns True if the argument is a string that represents a valid ISBN-10 code, False otherwise.

    >>> isISBN('9971502100')
    True
    >>> isISBN('9971502108')
    False
    >>> isISBN('53WKEFF2C')
    False
    >>> isISBN(4378580136)
    False
    """

    # note: isinstance is a built-in function of Python that returns a Boolean value that indicates whether the first
    #       argument is an object that has a data type equal to the second argument
    return (
        isinstance(code, str) and      # code must be a string
        len(code) == 10 and            # code must contain 10 characters
        code[:9].isdigit() and         # first nine characters must be digits
        checkdigit(code) == code[-1]   # check digit must be correct
    )

def checkdigit(code):

    """
    Computes the check digit for a given string that contains the first nine digits of an ISBN-10 code. A string
    representation of the check digit is returned, with the value 10 represented as the letter X.

    >>> checkdigit('9971502100')
    '0'
    >>> checkdigit('9971502108')
    '0'
    """

    # compute check digit
    check = sum(index * int(digit) for index, digit in enumerate(code[:9], start=1)) % 11

    # convert check digit into string representation
    return 'X' if check == 10 else str(check)

if __name__ == '__main__':
    import doctest
    doctest.testmod()

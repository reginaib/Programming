class ISBN13:

    """
    >>> code = ISBN13(9780136110675)
    >>> print(code)
    978-0-13611067-5
    >>> code
    ISBN13(9780136110675, 1)
    >>> code.isvalid()
    True
    >>> code.asISBN10()
    '0-13611067-3'

    >>> ISBN13(9780136110675, 6)
    Traceback (most recent call last):
    AssertionError: invalid ISBN code
    """

    def __init__(self, code, length=1):

        # check validity of arguments
        message = 'invalid ISBN code'
        assert isinstance(code, int), message
        assert isinstance(length, int) and 1 <= length <= 5, message

        # object properties: ISBN-code and length of country group
        # convert to string of 13 characters with leading zeros
        self.code = str(code).zfill(13)
        self.length = length

    def __int__(self):

        return int(self.code)

    def __str__(self):

        # return formatted representation of ISBN-code
        c = self.code
        return f'{c[:3]}-{c[3:3 + self.length]}-{c[3 + self.length:-1]}-{c[-1]}'

    def __repr__(self):

        # return string containing a Python expression that creates a new
        # object having the same internal state as the current object
        return f'ISBN13({int(self.code)}, {self.length})'

    def isvalid(self):

        def checkdigit(code):

            # compute ISBN-13 check digit
            check = sum((3 if index % 2 else 1) * int(digit) for index, digit in enumerate(code[:12]))

            # convert check digit into string representation
            return str((10 - check) % 10)

        # check validity of check digit
        return self.code[12] == checkdigit(self.code)

    def asISBN10(self):

        def checkdigit(code):

            # compute ISBN-10 check digit
            check = sum((index * int(digit) for index, digit in enumerate(code[:9], start=1))) % 11

            # convert check digit into string representation
            return 'X' if check == 10 else str(check)

        # return no result for invalid ISBN-13 codes
        if not self.isvalid() or str(self.code)[:3] != '978':
            return None

        # convert ISBN-13 code into ISBN-10 code
        code = self.code[3:-1]
        check = checkdigit(code)
        return f'{code[:self.length]}-{code[self.length:]}-{check}'

if __name__ == '__main__':
    import doctest
    doctest.testmod()

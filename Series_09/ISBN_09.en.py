import urllib.request

def isISBN13(code):

    """
    Returns a Boolean value that indicates whether the given ISBN-13 code is valid.

    >>> isISBN13('9789743159664')
    True
    >>> isISBN13('9787954527409')
    False
    >>> isISBN13('8799743159665')
    False
    """

    def checkdigit(code):

        """Helper function that computes the ISBN-13 check digit."""

        # compute the check digit
        check = sum((3 if index % 2 else 1) * int(digit) for index, digit in enumerate(code[:12]))

        # convert the check digit into a single digit
        return str((10 - check) % 10)

    # check whether the given code is a string
    if not isinstance(code, str):
        return False

    # check whether the given code contains 13 characters
    if len(code) != 13:
        return False

    # check prefix of the given code
    if code[:3] not in {'978', '979'}:
        return False

    # check whether first nine characters of the given code are digits
    if not code[:12].isdigit():
        return False

    # check the check digit
    return checkdigit(code) == code[-1]

def remove_tags(s):

    """
    Removes all XML tags from the given string and then removes all leading and
    trailing whitespace.

    >>> remove_tags(' <Title> The Practice of Computing using <b>Python</b> </Title> ')
    'The Practice of Computing using Python'
    """

    # remove all XML tags from the given string
    start = s.find('<')
    while start >= 0:
        stop = s.find('>', start + 1)
        if stop == -1:
            stop = len(s)
        s = s[:start] + s[stop + 1:]
        start = s.find('<')

    # remove leading and trailing whitespace and returns the modified string
    return s.strip()

def display_book_info(code):

    """
    >>> display_book_info('9780136110675')
    Title: The Practice of Computing using Python
    Authors: William F Punch, Richard Enbody
    Publisher: Addison Wesley
    >>> display_book_info('9780136110678')
    Wrong ISBN-13 code
    """

    # remove leading and trailing whitespace characters from code
    code = code.strip()

    # check validity of ISBN-13 code
    if not isISBN13(code):

        # print error message in case given ISBN-13 code is invalid
        print('Wrong ISBN-13 code')

    else:

        # construct URL of imitated ISBNdb.com that provides information about the book with the given ISBN-13 code
        url = f'https://pythia.ugent.be/pythia-share/exercises/isbn9/books.php?isbn={code}'

        # extract and output selected book information from XML
        with urllib.request.urlopen(url) as info:
            for line in info:
                line = line.decode('utf-8')
                if line.startswith('<Title>'):
                    print(f'Title: {remove_tags(line)}')
                elif line.startswith('<AuthorsText>'):
                    print(f'Authors: {remove_tags(line).rstrip(", ")}')
                elif line.startswith('<PublisherText '):
                    print(f'Publisher: {remove_tags(line).rstrip(", ")}')

if __name__ == '__main__':
    import doctest
    doctest.testmod()

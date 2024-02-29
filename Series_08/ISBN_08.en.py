def isISBN13(code):

    """
    Checks whether the given ISBN-13 code is valid.

    >>> isISBN13('9789743159664')
    True
    >>> isISBN13('9787954527409')
    False
    >>> isISBN13('8799743159665')
    False
    """

    def check_digit(code):

        """
        Helper function that computes the ISBN-13 check digit.
        """

        # compute check digit
        check = sum((3 if index % 2 else 1) * int(digit) for index, digit in enumerate(code[:12]))

        # convert check digit into a single digit
        return str((10 - check) % 10)

    # check whether given code is a string
    if not isinstance(code, str):
        return False

    # check whether given code contains 13 characters
    if len(code) != 13:
        return False

    # check prefix of given code
    if code[:3] not in {'978', '979'}:
        return False

    # check whether all characters of given code are digits
    if not code.isdigit():
        return False

    # check the check digit
    return check_digit(code) == code[-1]

def overview(codes):

    """
    >>> codes = [
    ...    '9789743159664', '9785301556616', '9797668174969', '9781787559554',
    ...    '9780817481461', '9785130738708', '9798810365062', '9795345206033',
    ...    '9792361848797', '9785197570819', '9786922535370', '9791978044523',
    ...    '9796357284378', '9792982208529', '9793509549576', '9787954527409',
    ...    '9797566046955', '9785239955499', '9787769276051', '9789910855708',
    ...    '9783807934891', '9788337967876', '9786509441823', '9795400240705',
    ...    '9787509152157', '9791478081103', '9780488170969', '9795755809220',
    ...    '9793546666847', '9792322242176', '9782582638543', '9795919445653',
    ...    '9796783939729', '9782384928398', '9787590220100', '9797422143460',
    ...    '9798853923096', '9784177414990', '9799562126426', '9794732912038',
    ...    '9787184435972', '9794455619207', '9794270312172', '9783811648340',
    ...    '9799376073039', '9798552650309', '9798485624965', '9780734764010',
    ...    '9783635963865', '9783246924279', '9797449285853', '9781631746260',
    ...    '9791853742292', '9781796458336', '9791260591924', '9789367398012'
    ... ]
    >>> overview(codes)
    English speaking countries: 8
    French speaking countries: 4
    German speaking countries: 6
    Japan: 3
    Russian speaking countries: 7
    China: 8
    Other countries: 11
    Errors: 9
    """

    # construct histogram of registration groups
    groups = {group: 0 for group in range(11)}
    for code in codes:
        group = int(code[3]) if isISBN13(code) else 10
        groups[group] += 1

    # display overview
    print(f'English speaking countries: {groups[0] + groups[1]}')
    print(f'French speaking countries: {groups[2]}')
    print(f'German speaking countries: {groups[3]}')
    print(f'Japan: {groups[4]}')
    print(f'Russian speaking countries: {groups[5]}')
    print(f'China: {groups[7]}')
    print(f'Other countries: {groups[6] + groups[8] + groups[9]}')
    print(f'Errors: {groups[10]}')

if __name__ == '__main__':
    import doctest
    doctest.testmod()

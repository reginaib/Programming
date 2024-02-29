def side(letter, puzzle):
    for i, edge in enumerate(puzzle.split('-')):
        if letter in edge:
            return i
    return -1


def iscomplete(solution, puzzle):
    """
    >>> iscomplete('MYSTIC-CORAL-LIVER', 'YOI-RCM-VSA-LTE')
    True
    >>> iscomplete('DENIM-MAIZE-EGGPLANT', 'GND-IET-MZL-AP')
    True
    >>> iscomplete('GAINSBORO-ONYX-PEAR', 'BGY-NXE-PAO-SRI')
    True
    >>> iscomplete('KOBI-PLATINUM-ZOMP', 'TML-OZB-IUK-APN')
    True
    >>> iscomplete('DESERT-TEAL-LIVID', 'SIT-EVW-ADC-KLR')
    False
    >>> iscomplete('RUFOUS-SKOBELOFF', 'FL-XUM-SKE-BOR')
    False
    >>> iscomplete('DENIM-OPAL-MANDARIN', 'NMO-AI-LDR-EYP')
    False
    >>> iscomplete('BONE-SEPIA-BROWN', 'ODI-VAR-BEP-SNW')
    False
    """
    # Extract all the letters from the letter arrangement
    letters_in_puzzle = set(char for side in puzzle.split('-') for char in side)

    # Check if all letters from the letter arrangement are in the solution
    return all(letter in solution for letter in letters_in_puzzle)


def isconsecutive(solution):
    words = solution.split('-')
    for word1, word2 in zip(words, words[1:]):
        if word1[-1] != word2[0]:
            return False
    return True


def iscrossing(solution, puzzle):
    for word in solution.split('-'):
        for char1, char2 in zip(word, word[1:]):
            if side(char1, puzzle) == side(char2, puzzle):
                return False
    return True


def issolution(solution, puzzle):
    return iscomplete(solution, puzzle) and isconsecutive(solution) and iscrossing(solution, puzzle)
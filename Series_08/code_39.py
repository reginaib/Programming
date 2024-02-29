# https://dodona.be/nl/courses/2802/series/29674/activities/1186776322
def reverse(key):
    """
    >>> key = {
    ...     'U': 'SbSbSbSsS', 'Z': 'SsBsSbBsS', 'P': 'BbSsSsBsS', 'R': 'SsSbBsBsS',
    ...     'H': 'SsBbBsSsS', 'W': 'SbBsSsBsS', 'D': 'SbBsSsSsB', 'K': 'BsSsSsBbS',
    ...     '-': 'SsSbBsSsB', 'M': 'SbSsSbSbS', 'O': 'SsSbSsBsB', '7': 'SsSbSbSbS',
    ...     '+': 'BsSsBbSsS', '1': 'SsSsBbBsS', ' ': 'SsBsBbSsS', '.': 'SsBbSsBsS',
    ...     '/': 'SsSsBsBbS', 'V': 'SbSsBsBsS', 'X': 'SbSbSsSbS', 'C': 'SbSsBsSsB',
    ...     'Y': 'BsSsSbBsS', 'G': 'BsBsSsSbS', '4': 'SsBbSsSsB', 'Q': 'SsBsSbSsB',
    ...     'J': 'SsSsSsBbB', 'F': 'BsSsSbSsB', 'A': 'SsBsSsSbB', '6': 'BsSsSsSbB',
    ...     '2': 'BsBsSbSsS', '$': 'SsSsSbBsB', '0': 'BsSbBsSsS', 'N': 'SsBsBsSbS',
    ...     'I': 'BsSbSsSsB', '9': 'BbSsBsSsS', 'L': 'BsSbSsBsS', ',': 'SsSsBsSbB',
    ...     '5': 'BsSsBsSbS', 'B': 'BbBsSsSsS', '%': 'SsBsSsBbS', 'S': 'BsBbSsSsS',
    ...     '3': 'SbBsBsSsS', 'T': 'BbSsSsSsB', '*': 'SsSsBbSsB', 'E': 'SbSsSsBsB'
    ... }
    >>> reverse(key)
    {'SbSbSbSsS': 'U', 'SsBsSbBsS': 'Z', 'BbSsSsBsS': 'P', 'SsSbBsBsS': 'R', 'SsBbBsSsS': 'H', 'SbBsSsBsS': 'W', 'SbBsSsSsB': 'D', 'BsSsSsBbS': 'K', 'SsSbBsSsB': '-', 'SbSsSbSbS': 'M', 'SsSbSsBsB': 'O', 'SsSbSbSbS': '7', 'BsSsBbSsS': '+', 'SsSsBbBsS': '1', 'SsBsBbSsS': ' ', 'SsBbSsBsS': '.', 'SsSsBsBbS': '/', 'SbSsBsBsS': 'V', 'SbSbSsSbS': 'X', 'SbSsBsSsB': 'C', 'BsSsSbBsS': 'Y', 'BsBsSsSbS': 'G', 'SsBbSsSsB': '4', 'SsBsSbSsB': 'Q', 'SsSsSsBbB': 'J', 'BsSsSbSsB': 'F', 'SsBsSsSbB': 'A', 'BsSsSsSbB': '6', 'BsBsSbSsS': '2', 'SsSsSbBsB': '$', 'BsSbBsSsS': '0', 'SsBsBsSbS': 'N', 'BsSbSsSsB': 'I', 'BbSsBsSsS': '9', 'BsSbSsBsS': 'L', 'SsSsBsSbB': ',', 'BsSsBsSbS': '5', 'BbBsSsSsS': 'B', 'SsBsSsBbS': '%', 'BsBbSsSsS': 'S', 'SbBsBsSsS': '3', 'BbSsSsSsB': 'T', 'SsSsBbSsB': '*', 'SbSsSsBsB': 'E'}
    """
    return {v: k for k, v in key.items()}


def code39(sentence, key):
    """
    >>> key = {
    ...     'U': 'SbSbSbSsS', 'Z': 'SsBsSbBsS', 'P': 'BbSsSsBsS', 'R': 'SsSbBsBsS',
    ...     'H': 'SsBbBsSsS', 'W': 'SbBsSsBsS', 'D': 'SbBsSsSsB', 'K': 'BsSsSsBbS',
    ...     '-': 'SsSbBsSsB', 'M': 'SbSsSbSbS', 'O': 'SsSbSsBsB', '7': 'SsSbSbSbS',
    ...     '+': 'BsSsBbSsS', '1': 'SsSsBbBsS', ' ': 'SsBsBbSsS', '.': 'SsBbSsBsS',
    ...     '/': 'SsSsBsBbS', 'V': 'SbSsBsBsS', 'X': 'SbSbSsSbS', 'C': 'SbSsBsSsB',
    ...     'Y': 'BsSsSbBsS', 'G': 'BsBsSsSbS', '4': 'SsBbSsSsB', 'Q': 'SsBsSbSsB',
    ...     'J': 'SsSsSsBbB', 'F': 'BsSsSbSsB', 'A': 'SsBsSsSbB', '6': 'BsSsSsSbB',
    ...     '2': 'BsBsSbSsS', '$': 'SsSsSbBsB', '0': 'BsSbBsSsS', 'N': 'SsBsBsSbS',
    ...     'I': 'BsSbSsSsB', '9': 'BbSsBsSsS', 'L': 'BsSbSsBsS', ',': 'SsSsBsSbB',
    ...     '5': 'BsSsBsSbS', 'B': 'BbBsSsSsS', '%': 'SsBsSsBbS', 'S': 'BsBbSsSsS',
    ...     '3': 'SbBsBsSsS', 'T': 'BbSsSsSsB', '*': 'SsSsBbSsB', 'E': 'SbSsSsBsB'
    ... }
    >>> encoded = code39('Sulfur, so good.', key)
    >>> encoded
    'BsBbSsSsSsSbSbSbSsSsBsSbSsBsSsBsSsSbSsBsSbSbSbSsSsSsSbBsBsSsSsSsBsSbBsSsBsBbSsSsBsBbSsSsSsSsSbSsBsBsSsBsBbSsSsBsBsSsSbSsSsSbSsBsBsSsSbSsBsBsSbBsSsSsBsSsBbSsBsS'
    """
    code = []
    for char in sentence.upper():
        key_char = key[char]
        code.append(key_char)
    return 's'.join(code)


def decode39(encoded, key):
    """
    >>> key = {
    ...     'U': 'SbSbSbSsS', 'Z': 'SsBsSbBsS', 'P': 'BbSsSsBsS', 'R': 'SsSbBsBsS',
    ...     'H': 'SsBbBsSsS', 'W': 'SbBsSsBsS', 'D': 'SbBsSsSsB', 'K': 'BsSsSsBbS',
    ...     '-': 'SsSbBsSsB', 'M': 'SbSsSbSbS', 'O': 'SsSbSsBsB', '7': 'SsSbSbSbS',
    ...     '+': 'BsSsBbSsS', '1': 'SsSsBbBsS', ' ': 'SsBsBbSsS', '.': 'SsBbSsBsS',
    ...     '/': 'SsSsBsBbS', 'V': 'SbSsBsBsS', 'X': 'SbSbSsSbS', 'C': 'SbSsBsSsB',
    ...     'Y': 'BsSsSbBsS', 'G': 'BsBsSsSbS', '4': 'SsBbSsSsB', 'Q': 'SsBsSbSsB',
    ...     'J': 'SsSsSsBbB', 'F': 'BsSsSbSsB', 'A': 'SsBsSsSbB', '6': 'BsSsSsSbB',
    ...     '2': 'BsBsSbSsS', '$': 'SsSsSbBsB', '0': 'BsSbBsSsS', 'N': 'SsBsBsSbS',
    ...     'I': 'BsSbSsSsB', '9': 'BbSsBsSsS', 'L': 'BsSbSsBsS', ',': 'SsSsBsSbB',
    ...     '5': 'BsSsBsSbS', 'B': 'BbBsSsSsS', '%': 'SsBsSsBbS', 'S': 'BsBbSsSsS',
    ...     '3': 'SbBsBsSsS', 'T': 'BbSsSsSsB', '*': 'SsSsBbSsB', 'E': 'SbSsSsBsB'
    ... }
    >>> encoded = code39('Sulfur, so good.', key)
    >>> encoded
    'BsBbSsSsSsSbSbSbSsSsBsSbSsBsSsBsSsSbSsBsSbSbSbSsSsSsSbBsBsSsSsSsBsSbBsSsBsBbSsSsBsBbSsSsSsSsSbSsBsBsSsBsBbSsSsBsBsSsSbSsSsSbSsBsBsSsSbSsBsBsSbBsSsSsBsSsBbSsBsS'
    >>> decode39(encoded, key)
    'SULFUR, SO GOOD.'
    """
    rev_key = reverse(key)
    return ''.join(rev_key[encoded[i:i+9]] for i in range(0, len(encoded), 10))


if __name__ == '__main__':
    import doctest
    doctest.testmod()

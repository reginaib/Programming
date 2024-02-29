class Code39:

    """
    >>> code = Code39('code39.txt')
    >>> sentence = 'Sulfur, so good.'
    >>> encoded = code.encode(sentence)
    >>> encoded
    'BsBbSsSsSsSbSbSbSsSsBsSbSsBsSsBsSsSbSsBsSbSbSbSsSsSsSbBsBsSsSsSsBsSbBsSsBsBbSsSsBsBbSsSsSsSsSbSsBsBsSsBsBbSsSsBsBsSsSbSsSsSbSsBsBsSsSbSsBsBsSbBsSsSsBsSsBbSsBsS'
    >>> code.decode(encoded)
    'SULFUR, SO GOOD.'
    """

    def __init__(self, filename):

        self.letter2code = {}
        self.code2letter = {}
        for line in open(filename, 'r'):
            letter, code = line.rstrip('\n').split(':')
            self.letter2code[letter.upper()] = code
            self.code2letter[code] = letter.upper()

    def encode(self, sentence):

        return 's'.join(
            self.letter2code[character.upper()]
            for character in sentence
        )

    def decode(self, encoded):

        return ''.join(
            self.code2letter[encoded[index:index + 9]]
            for index in range(0, len(encoded), 10)
        )

if __name__ == '__main__':
    import doctest
    doctest.testmod()
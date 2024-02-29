# https://dodona.be/nl/courses/2802/series/29676/activities/1286590512
class Cipher:
    """
    >>> cipher = Cipher('pokemon.txt')
    >>> cipher.name(25)
    'PIKACHU'
    >>> cipher.name(83)
    'FARFETCHD'
    >>> cipher.name(474)
    'PORYGONZ'
    >>> cipher.name(538)
    'THROH'
    >>> cipher.name(642)
    'THUNDURUS'
    >>> cipher.name(811)
    'THWACKEY'
    >>> cipher.name(828)
    'THIEVUL'
    >>> cipher.name(994)
    'IRONMOTH'
    >>> cipher.name(1111)

    >>> cipher.decode('#0828.2 #0979.2 #0382.3 #0197.1 #0460.1 #0319.3 #0932.1 #0927.1 #0025.7')
    'THANKYOUASHANDPIKACHU'

    >>> cipher.longest_prefix('Thank You Ash And Pikachu')
    ({538, 642, 811, 828}, 2)
    >>> cipher.longest_prefix('ANKYOUASHANDPIKACHU') # doctest: +SKIP
    ({347, 979}, 2)
    >>> cipher.longest_prefix('KYOUASHANDPIKACHU') # doctest: +SKIP
    ({382}, 3)

    >>> cipher.encode_prefix('Thank You Ash And Pikachu')
    (828, 2)
    >>> cipher.encode_prefix('ANKYOUASHANDPIKACHU')
    (979, 2)
    >>> cipher.encode_prefix('KYOUASHANDPIKACHU')
    (382, 3)

    >>> cipher.encode('Thank You Ash And Pikachu')
    '#0828.2 #0979.2 #0382.3 #0197.1 #0460.1 #0319.3 #0932.1 #0927.1 #0025.7'
    >>> cipher.encode('#ThankYouAshAndPikachu')
    '#0828.2 #0979.2 #0382.3 #0197.1 #0460.1 #0319.3 #0932.1 #0927.1 #0025.7'
    """

    def __init__(self, location):
        with open(location, encoding='utf8') as file:
            self.key = {int(k): self.normalize(v) for k, v in (line.split(maxsplit=1) for line in file)}

    def normalize(self, t):
        return ''.join(character for character in t.upper() if character.isalpha())

    def name(self, id):
        return self.key.get(id)

    def decode(self, ciphertext):
        result = []
        for code in ciphertext.split():
            idx, ln = code[1:].split('.')
            result.append(self.key[int(idx)][:int(ln)])
        return ''.join(result)

    def longest_common_prefix(self, string, key):
        n = 0
        for n, (c1, c2) in enumerate(zip(string, key)):
            if c1 != c2:
                return n
        return n + 1

    def longest_prefix(self, t):
        ln = 0
        result = set()
        n = self.normalize(t)
        for k, v in self.key.items():
            x = self.longest_common_prefix(n, v)
            if x > ln:
                result = {k}
                ln = x
            elif x == ln:
                result.add(k)

        return result, ln

    def encode_prefix(self, t):
        uids, length = self.longest_prefix(t)
        assert length, 'encoding not possible'
        uid = min(uids, key=lambda uid: self.key[uid])
        return uid, length

    def encode(self, t):
        plaintext = self.normalize(t)
        codes = []
        while plaintext:
            uid, length = self.encode_prefix(plaintext)
            codes.append(f'#{uid:04d}.{length}')
            plaintext = plaintext[length:]
        return ' '.join(codes)


if __name__ == '__main__':
    import doctest
    doctest.testmod()

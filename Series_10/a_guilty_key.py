# https://dodona.be/nl/courses/2802/series/29676/activities/452312283
"""
>>> cipher = Cipher('ABCD', '1AX3S1M2PYZ')
>>> cipher.grid
[['-', 'A', 'X', '-'], ['-', '-', 'S', '-'], ['M', '-', '-', 'P'], ['Y', 'Z', '-', '-']]
>>> cipher.map
{'A': 'AB', 'X': 'AC', 'S': 'BC', 'M': 'CA', 'P': 'CD', 'Y': 'DA', 'Z': 'DB'}
>>> cipher.encode('spam')
'BCCDABCA'
>>> cipher.decode('BCCDABCA')
'SPAM'
>>> cipher.encode('eggs')
Traceback (most recent call last):
AssertionError: invalid message
>>> cipher.decode('BCCDBACA')
Traceback (most recent call last):
AssertionError: invalid message

>>> cipher02 = Cipher('HISPAYMENT', '14K1S2DL1NW4P2R1H3T3U2O6X3A1F6B1G4I1C2V1Y3E2M2J')
>>> cipher02.grid
[['-', '-', '-', '-', '-', '-', '-', '-', '-', '-'], ['-', '-', '-', '-', 'K', '-', 'S', '-', '-', 'D'], ['L', '-', 'N', 'W', '-', '-', '-', '-', 'P', '-'], ['-', 'R', '-', 'H', '-', '-', '-', 'T', '-', '-'], ['-', 'U', '-', '-', 'O', '-', '-', '-', '-', '-'], ['-', 'X', '-', '-', '-', 'A', '-', 'F', '-', '-'], ['-', '-', '-', '-', 'B', '-', 'G', '-', '-', '-'], ['-', 'I', '-', 'C', '-', '-', 'V', '-', 'Y', '-'], ['-', '-', 'E', '-', '-', 'M', '-', '-', 'J', '-'], ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-']]
>>> cipher02.map
{'K': 'IA', 'S': 'IM', 'D': 'IT', 'L': 'SH', 'N': 'SS', 'W': 'SP', 'P': 'SN', 'R': 'PI', 'H': 'PP', 'T': 'PE', 'U': 'AI', 'O': 'AA', 'X': 'YI', 'A': 'YY', 'F': 'YE', 'B': 'MA', 'G': 'MM', 'I': 'EI', 'C': 'EP', 'V': 'EM', 'Y': 'EN', 'E': 'NS', 'M': 'NY', 'J': 'NN'}
>>> cipher02.encode('Have Marble and Coyle telegraph for influential men from Delaware and Virginia.')
'PPYYEMNSNYYYPIMASHNSYYSSITEPAAENSHNSPENSSHNSMMPIYYSNPPYEAAPIEISSYESHAINSSSPEEIYYSHNYNSSSYEPIAANYITNSSHYYSPYYPINSYYSSITEMEIPIMMEISSEIYY'
>>> cipher02.decode('PPYYEMNSNYYYPIMASHNSYYSSITEPAAENSHNSPENSSHNSMMPIYYSNPPYEAAPIEISSYESHAINSSSPEEIYYSHNYNSSSYEPIAANYITNSSHYYSPYYPINSYYSSITEMEIPIMMEISSEIYY')
'HAVEMARBLEANDCOYLETELEGRAPHFORINFLUENTIALMENFROMDELAWAREANDVIRGINIA'
>>> cipher02.encode('Indications of weakening here.')
'EISSITEIEPYYPEEIAASSIMAAYESPNSYYIANSSSEISSMMPPNSPINS'
>>> cipher02.decode('EISSITEIEPYYPEEIAASSIMAAYESPNSYYIANSSSEISSMMPPNSPINS')
'INDICATIONSOFWEAKENINGHERE'
>>> cipher02.encode('Press advantage and watch Board.')
'SNPINSIMIMYYITEMYYSSPEYYMMNSYYSSITSPYYPEEPPPMAAAYYPIIT'
>>> cipher02.decode('SNPINSIMIMYYITEMYYSSPEYYMMNSYYSSITSPYYPEEPPPMAAAYYPIIT')
'PRESSADVANTAGEANDWATCHBOARD'
"""


class Cipher:
    def __init__(self, keyword, description):
        self.keyword = keyword
        self.description = description

    @property
    def grid(self):
        grid = ['-'] * len(self.keyword) ** 2
        shift = 0
        current = ''
        for d in self.description:
            if d.isdigit():
                current += d
            else:
                if current:
                    shift += int(current)
                    current = ''
                grid[shift] = d
                shift += 1
        return [grid[i:len(self.keyword)+i] for i in range(0, len(grid), len(self.keyword))]

    @property
    def map(self):
        mapping = {}
        for r, row in zip(self.keyword, self.grid):
            for c, char in zip(self.keyword, row):
                if char != '-':
                    mapping[char] = r + c
        return mapping

    def encode(self, message):
        encoded = []
        for char in message.upper():
            if char.isalpha():
                if char in self.map:
                    encoded.append(self.map[char])
                else:
                    raise AssertionError('invalid message')
        return ''.join(encoded)

    def decode(self, message):
        decoded = []
        for i in range(0, len(message), 2):
            bigram = message[i:i+2]
            found = False
            for char, bg in self.map.items():
                if bg == bigram:
                    decoded.append(char)
                    found = True
                    break
            if not found:
                raise AssertionError('invalid message')
        return ''.join(decoded)


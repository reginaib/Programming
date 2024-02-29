"""
>>> tile1 = Domino(3, 4)
>>> Domino(-1, 7)
Traceback (most recent call last):
AssertionError: invalid number of pips

>>> tile1 # -> __repr__ (the expression is represented)
Domino(3, 4)
>>> print(tile1) # -> str (call str())
+---+---+
|o  |o o|
| o |   |
|  o|o o|
+---+---+
>>> print(tile1.rotate())
+---+---+
|o o|o  |
|   | o |
|o o|  o|
+---+---+
>>> print(tile1)
+---+---+
|o  |o o|
| o |   |
|  o|o o|
+---+---+

>>> tile2 = Domino(1, 3)
>>> tile1 + tile2
Traceback (most recent call last):
AssertionError: domino tiles do not match
>>> print(tile2 + tile1)
+---+---+
|   |o o|
| o |   |
|   |o o|
+---+---+
>>> tile3 = tile1.rotate() + tile2.rotate() # -> __add__
>>> tile3
Domino(4, 1)
>>> print(tile3)
+---+---+
|o o|   |
|   | o |
|o o|   |
+---+---+
"""


class Domino:

    eyes = {
        0: '       ',
        1: '   o   ',
        2: 'o     o',
        3: 'o  o  o',
        4: 'o o o o',
        5: 'o ooo o',
        6: 'ooo ooo'
    }

    def __init__(self, left, right):
        assert (
            isinstance(left, int)
            and isinstance(right, int)
            and 0 <= left <= 6
            and 0 <= right <= 6
        ), 'invalid number of pips'

        self.left = left
        self.right = right

    def __repr__(self):
        return f'Domino({self.left}, {self.right})'

    def __str__(self):

        eyes_left = self.eyes[self.left]
        eyes_right = self.eyes[self.right]

        output = '+---+---+\n'
        output += f'|{eyes_left[:3]}|{eyes_right[:3]}|\n'
        output += f'| {eyes_left[3]} | {eyes_right[3]} |\n'
        output += f'|{eyes_left[-3:]}|{eyes_right[-3:]}|\n'
        output += '+---+---+'

        return output

    def rotate(self):
        return Domino(self.right, self.left)

    def __add__(self, other):
        assert self.right == other.left, 'domino tiles do not match'
        return Domino(self.left, other.right)


if __name__ == '__main__':
    import doctest
    doctest.testmod()

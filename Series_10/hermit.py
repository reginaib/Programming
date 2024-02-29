# https://dodona.be/nl/courses/2802/series/29676/activities/2146239081
"""
>>> board = Hermit(4)
>>> print(board)
. . . .
. . . .
. . . .
. . . .
>>> board.positions((0, 0), 'H')
{(0, 0), (0, 1)}
>>> board.isvalid('R', (0, 0))
True
>>> board.isvalid('R', (0, 1))
True
>>> print(board.move('R', (0, 0), 'H'))
R R . .
. . . .
. . . .
. . . .
>>> print(board.move('R', (1, 2), 'V'))
Traceback (most recent call last):
AssertionError: invalid move
>>> print(board.move('B', (0, 2), 'U').move('Y', (1, 2), 'U'))
R R B .
. . Y .
. . . .
. . . .
>>> print(board.move('R', (3, 1), 'U').move('Y', (3, 2), 'H'))
R R B .
. . Y .
. . . .
. R Y Y
>>> print(board.move('R', (1, 3), 'V').move('B', (2, 0), 'H'))
R R B .
. . Y R
B B . R
. R Y Y
>>> board.possible_moves()
{('Y', (1, 0), 'U'), ('Y', (3, 0), 'U')}
>>> print(board.move('Y', (3, 0), 'U'))
R R B .
. . Y R
B B . R
Y R Y Y
>>> board.possible_moves()
{('Y', (1, 0), 'U')}
>>> print(board.move('Y', (1, 0), 'U'))
R R B .
Y . Y R
B B . R
Y R Y Y
>>> board.possible_moves()
set()
"""


class Hermit:

    def __init__(self, dimension):
        self.dimension = dimension
        self.board = [['.' for _ in range(dimension)] for _ in range(dimension)]

    def __str__(self):
        return '\n'.join([' '.join(row) for row in self.board])

    def positions(self, position, placement):
        row, col = position
        positions = set()

        if placement == 'U':
            positions.add((row, col))
        elif placement == 'H':
            positions.add((row, col))
            positions.add((row, col + 1))
        elif placement == 'V':
            positions.add((row, col))
            positions.add((row + 1, col))

        return positions

    def isvalid(self, color, square):
        row, col = square
        if row < 0 or row >= self.dimension or col < 0 or col >= self.dimension:
            return False
        if self.board[row][col] != '.':
            return False
        for r in self.board[max(0, row - 1): row + 2]:
            for c in r[max(0, col - 1): col + 2]:
                if c == color:
                    return False
        return True

    def move(self, color, position, placement):
        assert (color, position, placement) in self.possible_moves(), 'invalid move'
        for r, c in self.positions(position, placement):
            self.board[r][c] = color
        return self

    def possible_moves(self):
        moves = set()
        for r in range(self.dimension):
            for c in range(self.dimension):
                for color in 'RBY':
                    if self.isvalid(color, (r, c)):
                        moves.add((color, (r, c), 'U'))
                        if self.isvalid(color, (r, c + 1)):
                            moves.add((color, (r, c), 'H'))
                        if self.isvalid(color, (r + 1, c)):
                            moves.add((color, (r, c), 'V'))
        return moves




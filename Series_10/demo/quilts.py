class Quilt:
    
    r"""
    >>> quilt = Quilt(2, 2, '//++')
    >>> print(quilt)
    //
    ++
    >>> quilt += Quilt(2, 2, '-\\||')
    >>> print(quilt)
    //-\
    ++||
    >>> quilt
    Quilt(2, 4, '//-\\++||')
    >>> quilt = quilt.rotate()
    >>> print(quilt)
    +\
    +\
    -|
    -/
    >>> quilt
    Quilt(4, 2, '+\\+\\-|-/')
    >>> quilt += Quilt(2, 2, '-\\||')
    Traceback (most recent call last):
    AssertionError: quilts do not have the same height
    >>> quilt = quilt.rotate()
    >>> print(quilt)
    ||++
    \-//
    >>> Quilt(2, 3, '++++')
    Traceback (most recent call last):
    AssertionError: invalid configuration
    >>> Quilt(2, 3, 'oxooXo')
    Traceback (most recent call last):
    AssertionError: invalid configuration
    """
    
    def __init__(self, rows, columns, pattern):
        
        assert len(pattern) == rows * columns, 'invalid configuration'
        for letter in pattern:
            assert letter in '\\/+*-|ox', 'invalid configuration' 
        
        self.rows = rows
        self.columns = columns
        self.pattern = pattern
        
    def getRow(self, row):
        
        assert 0 <= row < self.rows, 'invalid row-index'
        return self.pattern[row * self.columns:(row + 1) * self.columns]
    
    def getPatch(self, row, column):
        
        assert 0 <= row < self.rows, 'invalid row-index'
        assert 0 <= column < self.columns, 'invalid column-index'
        return self.pattern[row * self.columns + column]
        
    def __str__(self):
        
        return '\n'.join(self.getRow(row) for row in range(self.rows))       

    def __repr__(self):
        
        return 'Quilt({}, {}, {!r})'.format(
            self.rows, 
            self.columns, 
            self.pattern
        )
        
    def __add__(self, other):
        
        assert self.rows == other.rows, 'quilts do not have an equal height'
        
        # add two patterns together for a new pattern
        new_pattern = ''.join(
            self.getRow(row) + other.getRow(row) for row in range(self.rows)
        )
        
        return Quilt(self.rows, self.columns + other.columns, new_pattern)
    
    def rotate(self):
        
        def rotation(symbol):
            
            """
            Returns the rotated symbol
            """
            
            symbols = '\\/-|'
            rotations = '/\\|-'
            
            p = symbols.find(symbol)
            if p == -1:
                return symbol
            else:
                return rotations[p]
            
        # rotate pattern 90 degrees clockwise   
        new_pattern = ''.join(
            ''.join(
                rotation(self.getPatch(self.rows - i - 1, j))
                for i in range(self.rows)
            )
            for j in range(self.columns)
        )
        
        return Quilt(self.columns, self.rows, new_pattern)


if __name__ == '__main__':
    import doctest
    doctest.testmod()

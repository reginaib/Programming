class Leaf:
    
    """
    >>> leaf = Leaf('leaf.txt')
    >>> print(leaf)
    <BLANKLINE>
                                          ######                
                               #############   ##########       
                         #######                         #####  
                      #####                       ############# 
                   ####                       ####          ##  
                 ###                     #####              ##  
               ###                  #####                  ###  
             ###                ####                       ##   
            ##               ###                          ###   
           ##             ###                            ###    
          ##          ####                             ###      
         ##        ###                                ###       
         #     ####                                 ###         
        ##  ####                                 ####           
        #####                                 #####             
        ###                                #####                
        #####                        #######                    
        #   ##########################                          
    <BLANKLINE>
    >>> leaf.fill(5, 30)
    182
    >>> print(leaf)
    <BLANKLINE>
                                          ######                
                               #############...##########       
                         #######.........................#####  
                      #####.......................############# 
                   ####.......................####          ##  
                 ###.....................#####              ##  
               ###..................#####                  ###  
             ###................####                       ##   
            ##...............###                          ###   
           ##.............###                            ###    
          ##..........####                             ###      
         ##........###                                ###       
         #.....####                                 ###         
        ##..####                                 ####           
        #####                                 #####             
        ###                                #####                
        #####                        #######                    
        #   ##########################                          
    <BLANKLINE>
    >>> leaf.fill(8, 30)
    Traceback (most recent call last):
    AssertionError: bit must be empty
    >>> leaf.fill(15, 30)
    335
    >>> print(leaf)
    <BLANKLINE>
                                          ######                
                               #############...##########       
                         #######.........................#####  
                      #####.......................############# 
                   ####.......................####..........##  
                 ###.....................#####..............##  
               ###..................#####..................###  
             ###................####.......................##   
            ##...............###..........................###   
           ##.............###............................###    
          ##..........####.............................###      
         ##........###................................###       
         #.....####.................................###         
        ##..####.................................####           
        #####.................................#####             
        ###................................#####                
        #####........................#######                    
        #   ##########################                          
    <BLANKLINE>
    >>> leaf.clear()
    >>> print(leaf)
    <BLANKLINE>
                                          ######                
                               #############   ##########       
                         #######                         #####  
                      #####                       ############# 
                   ####                       ####          ##  
                 ###                     #####              ##  
               ###                  #####                  ###  
             ###                ####                       ##   
            ##               ###                          ###   
           ##             ###                            ###    
          ##          ####                             ###      
         ##        ###                                ###       
         #     ####                                 ###         
        ##  ####                                 ####           
        #####                                 #####             
        ###                                #####                
        #####                        #######                    
        #   ##########################                          
    <BLANKLINE>
    >>> leaf.cells()
    2
    >>> leaf.cellsize()
    258.5
    
    >>> victoria = Leaf('victoria.txt')
    >>> victoria.cells()
    242
    >>> victoria.cells(minimum=10)
    219
    >>> victoria.cells(minimum=20)
    213
    >>> victoria.cellsize()
    107.86363636363636
    >>> victoria.cellsize(minimum=10)
    118.74885844748859
    >>> victoria.cellsize(minimum=20)
    121.64319248826291

    >>> sample = Leaf('sample.txt')
    >>> sample.cells()
    2
    """
    
    def __init__(self, filename):
        
        # read leaf bitmap
        self._bitmap = [list(line.rstrip('\n')) for line in open(filename, 'r')]
            
        # constructed list of cell sizes
        self._cellsizes = None
            
    def __str__(self):
        
        """
        prints an ascii representation of the leaf, showing empty bits as
        spaces, filled bits as dots and border bits as pound signs
        """
        
        return '\n'.join(''.join(row) for row in self._bitmap)
    
    def fill(self, row, col):
        
        """
        fills the cell containing the empty bit at the given row and column and
        return the number of bits included in that cell
        """
        
        # check if given bit is empty
        assert self._bitmap[row][col] == ' ', 'bit must be empty'
        
        # flood fill cell containing the given bit and count the number of
        # bits that is filled
        bits, count = {(row, col)}, 0
        while bits:
            
            # select a random bit
            r, c = bits.pop()
            
            # fill selected bit with a dot
            self._bitmap[r][c] = '.'
            count += 1
            
            # add empty neighbours of selected bit to set of bits
            for dr, dc in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                if (
                    0 <= r + dr < len(self._bitmap) and
                    0 <= c + dc < len(self._bitmap[0]) and
                    self._bitmap[r + dr][c + dc] == ' '
                ):
                    bits.add((r + dr, c + dc))
            
        return count
    
    def clear(self):
        
        """
        empties all filled bits
        """
        
        # traverse each bit and empty filled bits
        for row in range(len(self._bitmap)):
            for col in range(len(self._bitmap[0])):
                if self._bitmap[row][col] == '.':
                    self._bitmap[row][col] = ' '

    def _analyze_cells(self, minimum, func=None):
        
        """
        helper method that allows a single implementation for the methods cells
        and cellsize; since the leaf bitmap is static, the list of cell sizes is
        only computed once and stored in the property cellsizes in order to
        speed up repeated analyses of the bitmap 
        """
        
        if self._cellsizes is None:
            
            # construct a list of cell sizes
            self._cellsizes = []
        
            # determine number of rows and columns
            rows, cols = len(self._bitmap), len(self._bitmap[0])

            # cells that contain bits on the border of the bitmap are never 
            # considered to be leaf cells and are thus filled beforehand
            for row in range(rows):
                for col in range(cols):
                    if (
                        (
                            row in (0, rows - 1) or  # first or last row 
                            col in (0, cols - 1)     # first or last column
                        )
                        and
                        self._bitmap[row][col] == ' '
                    ):
                        self.fill(row, col)
            
            # traverse bitmap left to right and top to bottom, and fill empty
            # cells that are encountered along the way
            for row in range(rows):
                for col in range(cols):
                    if self._bitmap[row][col] == ' ':
                        size = self.fill(row, col)
                        self._cellsizes.append(size)
            
            # empty filled cells to undo filling 
            self.clear()

        # a list of cell sizes that are not smallee than the minimal size is
        # returned if no aggregation function is supplied; otherwise the
        # aggregation function is applied to this list
        sizes = [size for size in self._cellsizes if size >= minimum]
        return func(sizes) if func else sizes
    
    def cells(self, minimum=1):
        
        """
        returns the number of cells having size not smaller than the given 
        minimal size
        """
        
        return self._analyze_cells(minimum, len)
        
    def cellsize(self, minimum=1):
        
        """
        returns the average size of the cells having size not smaller than the 
        given minimal size
        """
        
        # helper function that computes the average of a list of numbers
        def average(l):
            return sum(l) / len(l) if l else None
        
        return self._analyze_cells(minimum, average)
        
if __name__ == '__main__':
    import doctest
    doctest.testmod()
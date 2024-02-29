def purple(films):
    
    """
    >>> purple([(0, 0, 5, 5, 'R'), (10, 0, 5, 5, 'R'), (3, 2, 9, 2, 'B')])
    8
    """
    
    # set of cells covered by blue (resp. red) films
    blue, red = set(), set()
    
    # dictionary that maps color to corresponding set
    colors = {'B':blue, 'R':red}
    
    # create sets of cells that are covered by blue or red films
    for xpos, ypos, width, height, color in films:
        colors[color] |= {
            (x, y)
            for x in range(xpos, xpos + width)
            for y in range(ypos, ypos + height)
        }
        
    # cells in the intersection of the blue and red sets are covered
    # by films of both colors, which colors them purple
    return len(blue & red)

def cellophane(filename):

    """    
    >>> cellophane('cellophane.txt')
    8
    """
    
    # tranform file content into list that is formatted as the arguments
    # passed to the function purple
    films = []
    for line in open(filename, 'r'):
        line = line.split()
        films.append(
            (
                int(line[0][1:]), 
                int(line[1]), 
                int(line[2]), 
                int(line[3]), 
                line[0][0]
            )
        )
        
    # return the number of purple cells
    return purple(films)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
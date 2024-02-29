def grow(position, occupied):
    
    """
    >>> grow((0, 0), [(1, 0), (-1, 0), (0, -1)])
    (0, 1)
    >>> grow((0, 0), [(1, 0), (-1, 0), (0, 1)])
    (0, -1)
    >>> grow((0, 0), [(1, 0), (0, 1), (0, -1)])
    (-1, 0)
    >>> grow((0, 0), [(-1, 0), (0, 1), (0, -1)])
    (1, 0)
    >>> grow((0, 0), [(1, 0), (-1, 0), (0, 1), (0, -1)])
    """

    # determine positions of neighbours that are not yet occupied
    x, y = position
    steps = ((0, 1), (0, -1), (1, 0), (-1, 0))
    free_neighbours = [
        (x + dx, y + dy) for dx, dy in steps 
        if (x + dx, y + dy) not in occupied
    ]
            
    # randomly choose one of the free neighbours, if at least one exists
    from random import choice
    return choice(free_neighbours) if free_neighbours else None
    
def polymer(): 
    
    # initialize polymer: represented as a list of monomers
    monomers = [(0, 0)]
    occupied = set(monomers)
    
    # continue to randomly choose a next free neighbour until the polymer 
    # completely blocks itself
    next = grow(monomers[-1], occupied)
    while next:
        monomers.append(next)
        occupied.add(next)
        next = grow(next, occupied)
        
    # return the generated polymer
    return monomers

if __name__ == '__main__':
    import doctest
    doctest.testmod()
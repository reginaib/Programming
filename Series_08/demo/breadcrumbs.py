def reachable(point, maximum):
    
    """
    >>> reachable((0, 0), 0)
    True
    >>> reachable((10, 20), 3)
    True
    >>> reachable((2, 3), 4)
    False
    """
    
    return sum(int(x) for x in str(point[0]) + str(point[1]) if x.isdigit()) <= maximum

def neighbours(point):
    
    """
    >>> neighbours((0, 0))
    {(0, 1), (0, -1), (1, 0), (-1, 0)}
    >>> neighbours((4, 3))
    {(4, 2), (4, 4), (3, 3), (5, 3)}
    """
    
    return {
        (point[0] + dx, point[1] + dy)
        for dx, dy in ((0, 1), (0, -1), (-1, 0), (1, 0))
    }
    
def breadcrumbs(maximum):
    
    """
    >>> breadcrumbs(0)
    {(0, 0)}
    >>> breadcrumbs(2)
    {(0, 1), (-1, 1), (0, 0), (-1, 0), (0, -2), (0, 2), (2, 0), (-1, -1), (0, -1), (1, 0), (1, -1), (1, 1), (-2, 0)}
    >>> len(breadcrumbs(10))
    1121
    >>> len(breadcrumbs(19))
    102485
    """
    
    # initialize sets of visited points and points that need to be visited
    crumbs, border = set(), set()
    border.add((0, 0))
    
    # investigate border points
    while border:
        
        # select a next border point that needs to be investigated
        point = border.pop()
        
        # put a breadcrumb at this point
        crumbs.add(point)
        
        # add neighbouring points to the set of points that need to be visited
        # if they have no breadcrumb and are reachable
        for neighbour in neighbours(point):
            if neighbour not in crumbs and reachable(neighbour, maximum):
                border.add(neighbour)
                
    # return points having breadcrumbs
    return crumbs

if __name__ == '__main__':
    import doctest
    doctest.testmod()
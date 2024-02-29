def manhattanDistance(point1, point2):
    
    """
    >>> manhattanDistance((3, 5), (7, 9))
    8
    >>> manhattanDistance((12, 5), (3, 16))
    20
    """
    
    return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])

def critical(point, stations):
    
    """
    >>> critical((4, 3), [(1, 8), (4, 3), (6, 3), (6, 5)])
    False
    >>> critical((7, 4), [(1, 8), (4, 3), (6, 3), (6, 5)])
    True
    """
    
    # determine number of gas stations that are closest to the given point
    closest, count = None, 0
    for station in stations:
        distance = manhattanDistance(point, station)
        if closest == None or distance < closest:
            closest = distance
            count = 1
        elif distance == closest:
            count += 1
        
    # return whether there are multiple gas stations that are closest to the
    # given point    
    return count > 1

def manhattan(streets, avenues, stations):
    
    """
    >>> manhattan(10, 10, [(1, 8), (4, 3), (6, 3), (6, 5)])
    ****D*****
    ****D***P*
    *****D****
    *****DD***
    ***P*DDD**
    DDDDD***DD
    ***PDP****
    ****D*****
    ****D*****
    ****D*****
    """
    
    # print road map
    for street in range(streets):

        # determine next row of the grid
        text = ''
        for avenue in range(avenues):
            if (street, avenue) in stations:
                text += 'P'
            elif critical((street, avenue), stations):
                text += 'D'
            else:
                text += '*'

        # print next row of the grid
        print(text)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
def busgossip(routes):
    
    """
    >>> busgossip(((1, 2, 3, 4, 5), (5, 6, 7, 8), (3, 9, 6)))
    12
    >>> busgossip(((1, 2, 3), (2, 1, 3), (2, 4, 5, 3)))
    4
    >>> busgossip(((1, 2), (2, 1)))
    -1
    >>> busgossip(((11, 2, 2, 4, 8, 2, 2), (0, 11, 8), (11, 8, 10, 3, 11), (9, 2, 5, 0, 3), (4, 8, 2, 8, 1, 0, 5), (6, 8, 9), (2, 11, 3, 3)))
    8
    """
    
    # initialise rumors: each driver knows one rumor
    rumors = {bus:{bus} for bus in range(len(routes))}

    # drive around the city        
    minutes = 0
    while minutes <= 1440:
        
        # exchange rumors between busses that are at the same stop
        for bus1 in range(len(routes) - 1):
            stop1 = routes[bus1][minutes % len(routes[bus1])]
            for bus2 in range(bus1 + 1, len(routes)):
                stop2 = routes[bus2][minutes % len(routes[bus2])]
                if stop1 == stop2:
                    rumors[bus1].update(rumors[bus2])
                    rumors[bus2].update(rumors[bus1])
        
        # check whether all rumors have been exchanges
        if all(len(rumors[bus]) == len(routes) for bus in range(len(routes))):
            return minutes
        
        # go to the next stop
        minutes += 1

    return -1

if __name__ == '__main__':
    import doctest
    doctest.testmod()
def visible(posters):
    
    """
    >>> visible([(1, 4), (2, 5), (8, 3), (3, 2), (7, 4)])
    4
    >>> visible([(3, 5), (1, 4), (5, 6)])
    2
    >>> visible([(2, 1), (5, 1)])
    2
    """
    
    billboard = []
    for index, (start, width) in enumerate(posters):
        if len(billboard) < start + width:
            billboard += [None] * (start + width - len(billboard))
        billboard[start:start + width] = [index] * width
        
    return len({poster for poster in billboard if poster is not None})

if __name__ == '__main__':
    import doctest
    doctest.testmod()
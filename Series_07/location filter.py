def euclidean_distance(p1, p2):

    """
    >>> euclidean_distance((0, 0), (3, 4))
    5.0
    """

    x1, y1 = p1
    x2, y2 = p2
    return float(((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5)

def manhattan_distance(p1, p2):

    """
    >>> manhattan_distance((0, 0), (3,4))
    7.0
    """

    x1, y1 = p1
    x2, y2 = p2
    return float(abs(x1 - x2) + abs(y1 - y2))

def chessboard_distance(p1, p2):

    """
    >>> chessboard_distance((0, 0), (3, 4))
    4.0
    """

    x1, y1 = p1
    x2, y2 = p2
    return float(max(abs(x1 - x2), abs(y1 - y2)))

def location_filter(center, points, radius=1.0, distanceFunction=euclidean_distance):

    """
    >>> points = [(0, 0), (1, 0), (0, 1), (1, 1), (0, -1), (-1, 1)]
    >>> location_filter((0, 0), points)
    [(0, 0), (1, 0), (0, 1), (0, -1)]
    >>> location_filter((0, 0), points, 2)
    [(0, 0), (1, 0), (0, 1), (1, 1), (0, -1), (-1, 1)]
    >>> location_filter((0, 0), points, 1, chessboard_distance)
    [(0, 0), (1, 0), (0, 1), (1, 1), (0, -1), (-1, 1)]
    >>> location_filter((1, 0), points, 2, manhattan_distance)
    [(0, 0), (1, 0), (0, 1), (1, 1), (0, -1)]
    """

    filtered = []
    for point in points:
        if distanceFunction(center, point) <= radius:
            filtered.append(point)
    return filtered

    """
    # alternative solution using list comprehension
    
    return [point for point in points if distanceFunction(center, point) <= radius]
    """

if __name__ == '__main__':
    import doctest
    doctest.testmod()

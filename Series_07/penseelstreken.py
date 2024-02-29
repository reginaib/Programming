# https://dodona.be/en/courses/2802/series/29673/activities/1909833405
def floors(apartments):
    """
    >>> apartments = (1, 4, 3, 2, 3, 1)
    >>> floors(apartments)
    [[False, True, False, False, False, False], [False, True, True, False, True, False], [False, True, True, True, True, False], [True, True, True, True, True, True]]
    """
    result = []

    for current in range(max(apartments), 0, -1):
        result.append([value >= current for value in apartments])
    return result


def front_view(apartments, width = 3, distance = 1, apartment = "#", air = " "):
    """
    >>> apartments = (1, 4, 3, 2, 3, 1)
    >>> print(front_view(apartments, air='~'))
    ~~~~###~~~~~~~~~~~~~~~~
    ~~~~###~###~~~~~###~~~~
    ~~~~###~###~###~###~~~~
    ###~###~###~###~###~###
    >>> print(front_view(apartments, width=4, distance=0, apartment='<', air="-"))
    ----<<<<----------------
    ----<<<<<<<<----<<<<----
    ----<<<<<<<<<<<<<<<<----
    <<<<<<<<<<<<<<<<<<<<<<<<
    """
    result = []
    for values in floors(apartments):
        line = (air * distance).join((apartment if value else air) * width for value in values)
        result.append(line)
    return '\n'.join(result)


def brush_strokes(apartments):
    """
    >>> apartments = (1, 4, 3, 2, 3, 1)
    >>> brush_strokes(apartments)
    5
    """
    colors = 0
    previous = 0
    for current in apartments:
        if previous < current:
            colors += current - previous
        previous = current
    return colors


if __name__ == '__main__':
    import doctest
    doctest.testmod()

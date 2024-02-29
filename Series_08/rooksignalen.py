# https://dodona.be/nl/courses/2802/series/29674/activities/1401687450
def observed(watchtowers, network:dict):
    """
    >>> network = {1:{2, 5}, 2:{1, 5, 3}, 3:{2, 4}, 4:{3, 5, 6}, 5:{1, 2, 4}, 6:{4}}
    >>> observed({1, 2}, network)
    {3, 5}
    >>> observed({3, 4}, network)
    {2, 5, 6}
    """
    result = set()
    for value in watchtowers:
        result.update(network[value])
    return result - watchtowers


def distribution(watchtower, network):
    """
    >>> network = {1:{2, 5}, 2:{1, 5, 3}, 3:{2, 4}, 4:{3, 5, 6}, 5:{1, 2, 4}, 6:{4}}
    >>> distribution(1, network)
    3
    >>> distribution(4, network)
    2
    """
    fired = {watchtower}
    steps = 0
    while len(fired) != len(network):
        steps += 1
        fired.update(observed(fired, network=network))

    return steps


if __name__ == '__main__':
    import doctest
    doctest.testmod()

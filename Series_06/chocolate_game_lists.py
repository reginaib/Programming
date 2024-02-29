def chocolate_bars(bars):
    """
    >>> chocolate_bars([2, 9, 8, 2, 7])
    (2, 3)
    >>> chocolate_bars([1, 2, 3, 4, 3, 2, 1])
    (4, 3)
    """
    # number of bar that Alica and Bob has eaten so far
    alice, bob = [], []

    # Alice and Bob progressively eat all the bars
    for _ in range(len(bars)):
        # decide whether Alice or Bob eats the next bar
        if sum(alice) <= sum(bob):
            # Alice can eat her next bar
            alice.append(bars.pop(0))
        else:
            # Bob eats his next bar
            bob.append(bars.pop())

    # return of bars that Alice and Bob have eaten at the end of the game
    return len(alice), len(bob)


if __name__ == 'main':
    import doctest
    doctest.testmod()

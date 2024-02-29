def chocolate_bars(bars):
    """
    >>> chocolate_bars([2, 9, 8, 2, 7])
    (2, 3)
    >>> chocolate_bars([1, 2, 3, 4, 3, 2, 1])
    (4, 3)
    """
    # number of bar that Alica and Bob has eaten so far
    alice, bob = 0, 0

    # keep track when Alice and Bob are ready to eat next bar
    alice_ready, bob_ready = 0, 0

    # Alice and Bob progressively eat all the bars
    for _ in range(len(bars)):
        # decide whether Alice or Bob eats the next bar
        if alice_ready <= bob_ready:
            # Alice can eat her next bar
            alice_ready += bars[alice]
            alice += 1
        else:
            # Bob eats his next bar
            bob += 1
            bob_ready += bars[-bob]


    # return of bars that Alice and Bob have eaten at the end of the game
    return alice, bob


if __name__ == 'main':
    import doctest
    doctest.testmod()

def chocolateBars(bars):
    
    """
    >>> chocolateBars([])
    (0, 0)
    >>> chocolateBars([5])
    (1, 0)
    >>> chocolateBars([1, 1])
    (1, 1)
    >>> chocolateBars([2, 9, 8, 2, 7])
    (2, 3)
    >>> chocolateBars([1, 2, 3, 4, 3, 2, 1])
    (4, 3)
    """
    
    # number of chocolate bars already consumed by Alice and Bob
    alice, bob = 0, 0
    
    # time at which Alice and Bob are ready to start consuming their next 
    # chocolate bar
    alice_ready, bob_ready = 0, 0
    
    # eat all chocolate bars one by one
    for _ in range(len(bars)):
        
        if alice_ready <= bob_ready:
            alice_ready += bars[alice]
            alice += 1
        else:
            bob += 1
            bob_ready += bars[-bob]
            
    # return the number of chocolate bars consumed
    return alice, bob

if __name__ == '__main__':
    import doctest
    doctest.testmod()
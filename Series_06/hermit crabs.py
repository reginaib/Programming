def consecutive(shells):
    
    """
    >>> consecutive([7, 5, 4, 9, 6, 3, 8])
    True
    >>> consecutive((16, 13, 18, 17, 15, 14, 20))
    False
    >>> consecutive((3, 4, 1, 6, 8, 7))
    False
    """
    
    # make new list that contains shell sizes in increasing order
    shells = sorted(shells)
    
    # check if shell sizes form a sequence of consecutive integers
    for i in range(len(shells) - 1):
        if shells[i + 1] - shells[i] != 1:
            return False
     
    # shell sizes form a sequence of consecutive integers
    return True

    

def goldilocks(shells):
    
    """
    >>> goldilocks([7, 5, 4, 9, 6, 3, 8])
    >>> goldilocks((16, 13, 18, 17, 15, 14, 20))
    19
    >>> goldilocks((3, 4, 1, 6, 8, 7))
    """
    
    # make new list that contains shell sizes in increasing order
    shells = sorted(shells)
    
    # check if single shell can make sequence of consecutive shells
    missing = None
    for i in range(len(shells) - 1):
        if shells[i + 1] - shells[i] != 1:
            if shells[i + 1] - shells[i] == 2:
                if missing is None:
                    # first missing shell found
                    missing = shells[i] + 1
                else:
                    # second missing shell found
                    return None
            else:
                # sequence contains gap that is not equal to one or two
                return None
        
    # return the missing shell (if found)
    return missing

def move1(shells):
    
    """
    >>> move1([7, 5, 4, 9, 6, 3, 8])
    [7, 5, 4, 9, 6, 3, 8]
    >>> move1((16, 13, 18, 17, 15, 14, 20))
    [16, 13, 18, 17, 15, 14, 20, 19]
    >>> move1((3, 4, 1, 6, 8, 7))
    [3, 4, 1, 6, 8, 7]
    """
    
    # copy shells into a new list 
    shells = list(shells)

    # append missing shell to the end of the list if that establishes a 
    # sequence of consecutive shells 
    move2(shells)
        
    # return new list that may have been completed with the missing shell
    return shells

def move2(shells):
    
    """
    >>> shells = [7, 5, 4, 9, 6, 3, 8]
    >>> move2(shells)
    >>> shells
    [7, 5, 4, 9, 6, 3, 8]

    >>> shells = [16, 13, 18, 17, 15, 14, 20]
    >>> move2(shells)
    >>> shells
    [16, 13, 18, 17, 15, 14, 20, 19]

    >>> shells = [3, 4, 1, 6, 8, 7]
    >>> move2(shells)
    >>> shells
    [3, 4, 1, 6, 8, 7]
    """
    
    # append missing shell to the end of the list if that establishes a 
    # sequence of consecutive shells
    missing = goldilocks(shells)
    if missing is not None:
        shells.append(missing)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
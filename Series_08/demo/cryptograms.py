def cryptogram(crypto, solution):
    
    """
    >>> puzzle = 'Qmvrbwlf xwkd iopzlw vf zml pcwvfxzvyl.'
    >>> solution = 'Ch?ld??? ??ow fas??r ?n ??? ?p?i?gt?me.'
    >>> cryptogram(puzzle, solution)
    'Children grow faster in the springtime.'
    
    >>> puzzle = 'Zhp suxobpuw sbmtkopw Nxwkdnx.'
    >>> solution = '?h? p?n???a? ?rod?ces I???l??.'
    >>> cryptogram(puzzle, solution)
    '?he pancreas prod?ces Ins?lin.'

    >>> puzzle = 'Jujso ldmtq wyjqi tvadi ltek tq lads tw t wcqnej xjee.'
    >>> solution = '?v?ry ??ma? ?p??? ?bout h??f ?? ???? ?s ? ??ng?e c?l?.'
    >>> cryptogram(puzzle, solution)
    'Every human spent about half an hour as a s?ngle cell.'

    >>> puzzle = "V atult'a amrdd qvl zr nrbrqbrn zx v wumvl v medr vivx."
    >>> solution = "? ????k's ???l? ??n ?? ??t???ed ?y a hum?? ? ?i?? ?w??."
    >>> cryptogram(puzzle, solution)
    "A skunk's smell ?an ?e dete?ted ?y a human a mile away."
    """
    
    # check whether given cryptogram and solution have the same number of
    # arguments
    assert len(crypto) == len(solution), 'invalid arguments'
    
    # construct mapping between letters
    mapping = {
        l1:l2
        for l1, l2 in zip(crypto.lower(), solution.lower())
        if l1.isalpha() and l2 != '?'
    }

    def map(c):
        
        """
        Uses mapping to convert a letter in its corresponding letter, while 
        preserving uppercase and lowercase.
        """
        
        if c.lower() in mapping:
            letter = mapping[c.lower()]
            if c.isupper():
                letter = letter.upper()
        elif c.isalpha():
            letter = '?' 
        else:
            letter = c

        return letter
            
    # apply mapping between letters
    return ''.join(map(letter) for letter in crypto)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
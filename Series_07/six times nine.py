def evaluation(expression, base=10):
    
    """
    >>> evaluation('6 * 9', 13)
    54
    >>> evaluation('42', 13)
    54
    >>> evaluation('17 + 33 * 56', 23)
    8742
    >>> evaluation('41 * 42', 23)
    8742
    >>> evaluation('3 + 6 * 99' , 11)
    651
    >>> evaluation('3 + (6 * 99)' , 11)
    651
    """
    
    # rewrite expression so that all numbers are converted into their decimal
    # representation
    decimal, number = '', ''
    for character in expression:
        if character.isdigit():
            number += character
        else:
            if number:
                decimal += str(int(number, base))
                number = ''
            decimal += character

    # if the expression ends with a digit, the final number must be added to the
    # rewritten expressing having decimal values
    if number:
        decimal += str(int(number, base))

    return eval(decimal)

def numeralSystem(expression):
    
    """
    >>> numeralSystem('6 * 9 = 42')
    13
    >>> numeralSystem('17 + 33 * 56 = 41 * 42')
    23
    """
    
    # digit having maximal value across all numbers in the 
    # expression determines the smallest possible base
    base = max(int(c) for c in expression if c.isdigit()) + 1

    # split expression in left-hand and right-hand side
    lhs, rhs = expression.split('=')
    
    # lookup smallest base in which equality of lhs and rhs holds    
    while (
        base <= 36 and 
        evaluation(lhs, base) != evaluation(rhs, base)
    ):
        base += 1
    
    if base <= 36:        
        return base

if __name__ == '__main__':
    import doctest
    doctest.testmod()
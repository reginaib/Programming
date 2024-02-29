def ispermutation(list):
    
    """
    >>> ispermutation([2, 5, 3, 1, 6, 4])
    True
    >>> ispermutation([1, 4, 2, 0, 5, 3])
    False
    >>> ispermutation([2, 5, 3, 8, 1, 6, 4])
    False
    """
    
    # check whether each number in the range from 1 up to and including n (the 
    # length of the list) occurs in the list
    for i in range(len(list)):
        if i + 1 not in list:
            return False
        
    # if each number bin the range from 1 up to and including n occurs, it 
    # automatically occurs just once
    return True

def permutator(permutation, objects):
    
    """
    >>> notes = [3, 4, 1, 2]
    >>> paintings = ['mona lisa', 'the scream', 'ghent altarpiece', 'the kiss']
    >>> paintings = permutator(notes, paintings)
    >>> paintings
    ['ghent altarpiece', 'the kiss', 'mona lisa', 'the scream']
    >>> paintings = permutator(notes, paintings)
    >>> paintings
    ['mona lisa', 'the scream', 'ghent altarpiece', 'the kiss']
    
    >>> notes = [14, 6, 15, 3, 4, 10, 1, 12, 5, 2, 7, 13, 8, 11, 9]
    >>> paintings = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    >>> paintings = permutator(notes, paintings)
    >>> paintings
    [7, 10, 4, 5, 9, 2, 11, 13, 15, 6, 14, 8, 12, 1, 3]
    >>> paintings = permutator(notes, paintings)
    >>> paintings
    [11, 6, 5, 9, 15, 10, 14, 12, 3, 2, 1, 13, 8, 7, 4]
    >>> paintings = permutator(notes, paintings)
    >>> paintings
    [14, 2, 9, 15, 3, 6, 1, 8, 4, 10, 7, 12, 13, 11, 5]
    """
    
    # check validity of arguments
    assert len(permutation) == len(objects), 'the number of notes must equal the number of paintings'
    assert ispermutation(permutation), 'first argument must represent permutation of numbers between 1 and n'
    
    # create a new list that assigns the given objects to their new location
    # according to the given permutation
    new_location = [None] * len(objects)
    for i, object in enumerate(objects):
        new_location[permutation[i] - 1] = object

    # return given objects in their rearranged order 
    return new_location

def closingday(permutation):

    """
    >>> notes = [3, 4, 1, 2]
    >>> closingday(notes)
    2
    >>> notes = [14, 6, 15, 3, 4, 10, 1, 12, 5, 2, 7, 13, 8, 11, 9]
    >>> closingday(notes)
    60
    """
        
    # determine paintings on the second day; we also use the permutation to
    # indicate the original order of the paintings on the first day
    day, paintings = 1, permutator(permutation, permutation)
    
    # determine order of the paintings on the next days until the paintings are
    # again in their original order as on the opening day
    while paintings != permutation:
        day += 1
        paintings = permutator(permutation, paintings)
        
    # return closing day
    return day

if __name__ == '__main__':
    import doctest
    doctest.testmod()
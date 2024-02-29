def validKey(key):
    
    """
    >>> validKey('jfbqpwcvuamozhilgrxtkndesy')
    True
    >>> validKey('jfbqpwcxvuamozhilgrxtkndesy')
    False
    >>> validKey('jfbqpwvuamozhilgrxtkndesy')
    False
    >>> validKey('jfbqpwxvuamozhilgrxtkndesy')
    False
    """

    # given key must have data type string    
    if not isinstance(key, str):
        return False
    
    # given key must be permutation of all lowercase letters of the alphabet
    import string
    return sorted(key) == list(string.ascii_lowercase)    

def encode(word, key):
    
    """
    >>> encode('bakery', 'jfbqpwcvuamozhilgrxtkndesy')
    'fjmprs'
    >>> encode('butchery', 'jfbqpwcvuamozhilgrxtkndesy')
    'fktbvprs'
    >>> encode('bullet', 'jfbqpwcvuamozhilgrxtkndesy')
    'fkoopt'
    >>> encode('bakery', 'jfbqpwxvuamozhilgrxtkndesy')
    Traceback (most recent call last):
    AssertionError: invalid key
    """
    
    # check if key is valid
    assert validKey(key), 'invalid key'
        
    # apply substitution cipher
    import string
    return word.translate(str.maketrans(string.ascii_lowercase, key))

    """
    alternative solution:
    
    return ''.join(key[ord(letter) - ord('a')] for letter in word.lower())
    """

def hasAlphabeticOrder(word):
    
    """
    >>> hasAlphabeticOrder('bakery')
    False
    >>> hasAlphabeticOrder('fjmprs')
    True
    >>> hasAlphabeticOrder('bullet')
    False
    >>> hasAlphabeticOrder('fkoopt')
    True
    """
    
    # are there any successive letters that are not in alphabetic order?
    return all(
        word[index].lower() <= word[index + 1].lower()
        for index in range(len(word) - 1)
    )
    
    """
    alternative solution:
    
    for index in range(len(word) - 1):
        if word[index].lower() > word[index + 1].lower():
            return False
        
    # all letters are in alphabetic order
    return True
    """

def score(key, fl):
    
    """
    >>> score('jfbqpwcvuamozhilgrxtkndesy', 'six-letter-words.txt')
    60
    >>> score('idsxvaqtobuefpgcjwzrkmhnyl', 'six-letter-words.txt')
    474
    """

    # count the number of words that have their letters in alphabetic order 
    # after encoding; in doing so, we make use of the fact that the value True
    # has value 1 and the value False has value 0
    return sum(
        hasAlphabeticOrder(encode(word.strip(), key)) 
        for word in open(fl, 'r')
    )

if __name__ == '__main__':
    import doctest
    doctest.testmod()
def T9(word):
    
    """
    >>> T9('banner')
    '226637'
    >>> T9('succes')
    '782237'
    >>> T9('rubber')
    '782237'
    """
    
    def key(letter):
        
        """
        >>> key('B')
        '2'
        >>> key('z')
        '9'
        """
        
        # lookup position of letter in the alphabet
        position = ord(letter.lower()) - ord('a') 
    
        # return digit at corresponding position
        return '22233344455566677778889999'[position]

    # convert letters of word to corresponding combination
    # of keys on mobile phone keyboard 
    return ''.join(key(letter) for letter in word)

def mobileSynonyms(word1, word2):
    
    """
    >>> mobileSynonyms('succes', 'rubber')
    True
    >>> mobileSynonyms('Monday', 'Friday')
    False
    """
    
    return T9(word1) == T9(word2)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
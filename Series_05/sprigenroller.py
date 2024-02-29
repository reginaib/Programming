def distort_word(word):
    
    """
    Shuffles all letters in a given word, except for
    the first and the last letter of the word.
    
    >>> distort_word('monty')
    'motny'
    
    >>> distort_word('python')
    'pothyn'    
    """

    from random import randint

    # words having less then four letters remain
    # unchanged after distortion    
    if len(word) < 4:
        return word
    
    # determine permutation of letters
    s, p = word[1:-1], ''
    while s:
        pos = randint(0, len(s) - 1)
        p += s[pos]
        s = s[:pos] + s[pos + 1:]
    
    # return distorted word
    return word[0] + p + word[-1]

def distort_sentence(sentence):
    
    """
    Shuffles the letters of all words in a given sentence,
    each time retaining the first and last letter of the word.

    >>> distort_sentence('Nudge, nudge, wink, wink. Know what I mean?')
    'Nugde, ngude, wnik, wnik. Konw what I maen?'
    
    >>> distort_sentence('Nobody expects the Spanish inquisition!')
    'Nbdooy epxtces the Snpasih iiiitqnsoun!'
    
    >>> distort_sentence("He's not the Messiah - he's a very naughty boy.")
    "He's not the Mseasih - he's a vrey nhaugty boy."
    """

    word, distorted = '', ''
    for character in sentence:
        if character.isalpha():
            word += character
        else:
            if word:
                distorted += distort_word(word)
            distorted += character
            word = ''

    # final word possibly still needs to be processed
    if word:
        distorted += distort_word(word)
    
    # return distorted sentence
    return distorted
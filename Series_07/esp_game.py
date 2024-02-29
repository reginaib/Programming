# https://dodona.be/nl/courses/2802/series/29673/activities/1678755178
import random


def taboo_length(words, minimum=0, maximum=None):
    """
    >>> words = ['forest', 'meadow', 'scenery', 'hills']
    >>> taboo_length(words)
    3
    >>> taboo_length(words, minimum=2)
    4
    >>> taboo_length(words, maximum=3)
    1
    >>> taboo_length(words, minimum=2, maximum=3)
    3
    >>> taboo_length(words, minimum=-2, maximum=6)
    1
    """
    if minimum < 0 or minimum > len(words):
        minimum = 0

    if maximum is None or maximum > len(words) or maximum < minimum:
        maximum = len(words)

    return random.randint(minimum, maximum)


def taboo_words(words, minimum=0, maximum=None):
    """
    >>> taboo_words(words)
    ['forest', 'hills', 'meadow', 'scenery']
    >>> taboo_words(words, minimum=2)
    ['forest', 'meadow', 'scenery']
    >>> taboo_words(words, maximum=3)
    ['forest', 'hills', 'meadow']
    >>> taboo_words(words, minimum=2, maximum=3)
    ['hills', 'meadow', 'scenery']
    >>> taboo_words(words, minimum=-2, maximum=6)
    ['forest', 'hills', 'meadow', 'scenery']
    """
    return sorted(random.sample(words, taboo_length(words, minimum=minimum, maximum=maximum)),
                  key=lambda word: word.lower())


# https://dodona.be/nl/courses/2802/series/29674/activities/2046492002
def first_letter(name, tip):
    """
    >>> first_letter('🐇🐺🐵☃☃', {'☃': 'OLAF', '🐇': 'BUGSBUNNY', '🐵': 'LOUIE', '🐺': 'AKELA'})
    'BALOO'
    >>> first_letter('🐸🐺🧜', {'🐸': 'KERMIT', '🐺': 'AKELA', '🧜': 'ARIEL'})
    'KAA'
    >>> first_letter('🧚☃👦', {'☃': 'OLAF', '👦': 'MOWGLI', '🧚': 'TINKERBELL'})
    'TOM'
    """
    result = []
    for value in name:
        if value in tip:
            result.append(tip[value][0])
        else:
            result.append(value)
    return ''.join(result)


def repeated_emoji(name, tip):
    """
    >>> repeated_emoji('😸🧸🧸🚗🚗🚗☃☃☃💰💰💰🐳🐳', {'☃': 'OLAF', '🐳': 'MONSTRO', '💰': 'SCROOGEMCDUCK', '😸': 'FELIXTHECAT', '🚗': 'LIGHTNINGMCQUEEN', '🧸': 'WINNIETHEPOOH'})
    'FIGARO'
    >>> repeated_emoji('❄🦊🦊🦊🐺🐺🐺🐭🐭🐭😸😸 🐺🐺🐘🦘🦘🐾🐾', {'❄': 'SNOWWHITE', '🐘': 'HATHI', '🐭': 'JERRY', '🐺': 'AKELA', '🐾': 'SNOOPY', '😸': 'FELIXTHECAT', '🦊': 'JOHNWORTHINGTONFOULFELLOW', '🦘': 'KANGA'})
    'SHERE KHAN'
    >>> repeated_emoji('👦👦👦🦗🦗❄❄🦆🦆🦆🚗🚗🐤🐤🐤-⭐⭐⭐🦊🦊🦊🐤🐤🐤-🧽🧽🐳🐳🐰🐰👧👧', {'❄': 'SNOWWHITE', '⭐': 'PATRICKSTAR', '🐤': 'TWEETY', '🐰': 'ROGERRABBIT', '🐳': 'MONSTRO', '👦': 'MOWGLI', '👧': 'SHANTI', '🚗': 'LIGHTNINGMCQUEEN', '🦆': 'DONALDDUCK', '🦊': 'JOHNWORTHINGTONFOULFELLOW', '🦗': 'JIMINY', '🧽': 'SPONGEBOBSQUAREPANTS'})
    'WINNIE-THE-POOH'
    """
    previous = None
    decoded = []
    count = 0
    for char in name:
        if char not in tip:
            if previous is not None:
                decoded.append(tip[previous][count])
                previous = None
                count = 0
            decoded.append(char)
        elif previous is None:
            previous = char
        elif char == previous:
            count += 1
        else:
            decoded.append(tip[previous][count])
            previous = char
            count = 0
    if previous:
        decoded.append(tip[previous][count])
    return ''.join(decoded)


def next_letter(name, tip):
    """
    >>> next_letter('🐶🧜🧜🐱🧜🧜🐵🦆', {'🐱': 'FIGARO', '🐵': 'LOUIE', '🐶': 'GOOFY', '🦆': 'DONALDDUCK', '🧜': 'ARIEL'})
    'GARFIELD'
    >>> next_letter('🐁☃🧸🐶🐵🧸', {'☃': 'OLAF', '🐁': 'MICKEYMOUSE', '🐵': 'LOUIE', '🐶': 'GOOFY', '🧸': 'WINNIETHEPOOH'})
    'MOWGLI'
    >>> next_letter('🐗🐵🐗🐅🐵', {'🐅': 'TIGGER', '🐗': 'PUMBAA', '🐵': 'LOUIE'})
    'PLUTO'
    >>> next_letter('🐼🐼🤓🐼🧜🐟🐼🐙🧜', {'🐙': 'URSULA', '🐟': 'DORY', '🐼': 'PO', '🤓': 'MINION', '🧜': 'ARIEL'})
    'POMPADOUR'
    """
    freq = {}
    decoded = []
    for char in name:
        if char in tip:
            if char in freq:
                freq[char] += 1
                decoded.append(tip[char][freq[char] % len(tip[char])])
            else:
                freq[char] = 0
                decoded.append(tip[char][freq[char]])
        else:
            decoded.append(char)
    return ''.join(decoded)


if __name__ == '__main__':
    import doctest
    doctest.testmod()

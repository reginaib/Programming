# https://dodona.be/nl/courses/2802/series/29673/activities/1232685540
def letter2digit(letter):
    """
    >>> letter2digit('c')
    '3'
    >>> letter2digit('e')
    '5'
    >>> letter2digit('i')
    '9'
    >>> letter2digit('s')
    's'
    """
    # n = ord(letter.lower()) - ord('a') + 1
    # if n < 10:
    #     return str(n)
    # return letter

    return str(ord(letter) - ord('a')+1) if letter < 'j' else letter

def digit2letter(character):
    """
    >>> digit2letter('3')
    'c'
    >>> digit2letter('5')
    'e'
    >>> digit2letter('9')
    'i'
    >>> digit2letter('s')
    's'
    """
    # if digit.isnumeric():
    #     return chr(ord('a') + int(digit) - 1)
    # return digit
    return chr(ord('a') + int(character)-1) if character.isdigit() else character


def disentangle(message, step_size):
    """
    >>> disentangle('abcdefghijklmnopqrstuvwxyz', 3)
    'adgjmpsvybehknqtwzcfilorux'
    >>> disentangle('abcdefghijklmnopqrstuvwxyz', 4)
    'aeimquybfjnrvzcgkoswdhlptx'
    >>> disentangle('abcdefghijklmnopqrstuvwxyz', 5)
    'afkpuzbglqvchmrwdinsxejoty'
    """
    # result = ''
    # for start in range(step_size):
    #     result += message[start::step_size]
    # return result
    return ''.join(message[start::step_size] for start in range(step_size))


def decode(message, step_size=3):
    """
    >>> decode('won8nt57on16ts588159rspt18u91rls2snu1olrr555ns13ts5ro')
    'whenthesailsarestrongashiphasnoreasontofearturbulence'
    >>> decode('won8ZT MnJWOM Rt5M7o n16ts5 88159r spKVt1 8u91rl s2snAu 1olrr5 55ns13 tsAIJH V5ro')
    'whenthesailsarestrongashiphasnoreasontofearturbulence'
    >>> decode('tol2r859 515skr9s n55n5ots 51tot44', step_size=5)
    'theseadoesnotliketoberestrained'
    >>> decode('tol2ZTMr JWOMR85M 9515skr9 sn55n5ot KVs51tot 44', 5)
    'theseadoesnotliketoberestrained'
    """
    # discard all characters that are no digits or lowercase letters
    # preprocessed = ''.join(char for char in message if char.islower() or char.isdigit())
    #
    # decoded = ''.join(digit2letter(char) for char in disentangle(preprocessed, step_size))
    # return decoded

    message = ''.join(digit2letter(character)
                    for character in message
                    if (character.isdigit() and character != '0') or character.islower()
                    )
    return disentangle(message, step_size)

def entangle(message, step_size):
    """
    >>> entangle('abcdefghijklmnopqrstuvwxyz', 3)
    'ajsbktcludmvenwfoxgpyhqzir'
    >>> entangle('abcdefghijklmnopqrstuvwxyz', 4)
    'ahoubipvcjqwdkrxelsyfmtzgn'
    >>> entangle('abcdefghijklmnopqrstuvwxyz', 5)
    'aglqvbhmrwcinsxdjotyekpuzf'
    """
    result = [None] * len(message)
    n = 0
    step = 1
    for c in message:
        if n >= len(message):
            n = step
            step += 1
        result[n] = c
        n += step_size
    return ''.join(result)


def encode(message, step_size=3):
    """
    >>> encode('When the sails are strong a ship has no reason to fear turbulence.')
    'won8nt57on16ts588159rspt18u91rls2snu1olrr555ns13ts5ro'
    >>> encode('The sea does not like to be restrained.', step_size=5)
    'tol2r859515skr9sn55n5ots51tot44'
    """

    preprocessed = []
    for c in message:
        if c.isalpha():
            c = c.lower()
            if c < 'j':
                preprocessed.append(str(ord(c)-ord('a')+1))
            else:
                preprocessed.append(c)
    return entangle(''.join(preprocessed), step_size=step_size)



if __name__ == '__main__':
    import doctest
    doctest.testmod()

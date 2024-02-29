"""
>>> key = read_key('valknut.txt')
>>> key['W']
(2, 6)
>>> key['h']
(3, 8)
>>> key[' ']
(6, 8)
>>> key['.']
(2, 7)

>>> symbols2digits("Where wolf's ears are, wolf's teeth are near.", key)
'263863356368227752646124686325352468253563876822775264612468326363323868253563689463253527'
>>> symbols2digits("Where wolf's ears are, wolf's teeth are near.", key, swap=True)
'628336533686227725461642863652534286525336788622772546164286233636238386525336864936525372'

>>> grid = make_grid(key)
>>> grid
{1: 'mZkqUpMKE', 2: 'BwRsaW.DQ', 3: '|tVCr7Th"', 4: 'yG%_u#L(&', 5: '3lXHIcOPi', 6: "'-efY9$ 2", 7: 'jS80@zo:b', 8: ')g;N54,xd', 9: 'J1Fn?Av6!'}

>>> digits2symbols('263863356368227752646124686325352468253563876822775264612468326363323868253563689463253527', grid)
"Where wolf's ears are, wolf's teeth are near."
>>> digits2symbols('628336533686227725461642863652534286525336788622772546164286233636238386525336864936525372', grid, swap=True)
"Where wolf's ears are, wolf's teeth are near."

>>> encode("Where wolf's ears are, wolf's teeth are near.", key)
'-;7X74woa#pG47lXG4lX7:4woa#pG4R77R;4lX74&7lXS'

>>> decode('-;7X74woa#pG47lXG4lX7:4woa#pG4R77R;4lX74&7lXS', key)
"Where wolf's ears are, wolf's teeth are near."
"""
from collections import defaultdict


def read_key(location):
    dictionaty = {}
    with open(location, encoding='utf8') as f:
        for line in f:
            k, i, j = line.rstrip('\n').split('\t')
            dictionaty[k] = (int(i), int(j))
    return dictionaty


def symbols2digits(symbols, key, swap=False):
    result = []
    for c in symbols:
        i, j = key[c]
        if swap:
            result.append(j)
            result.append(i)
        else:
            result.append(i)
            result.append(j)
    return ''.join(str(c) for c in result)

    # result = ''
    # for c in symbols:
    #     i, j = key[c]
    #     if swap:
    #         result += f'{j}{i}'
    #     else:
    #         result += f'{i}{j}'
    # return result


def make_grid(key):
    result = defaultdict(dict)
    for k, (i, j) in key.items():
        result[i][j] = k
    return {i: ''.join(result[i][j] for j in range(1, 10)) for i in range(1, 10)}


def digits2symbols(seq, grid, swap=False):
    result = []
    for i, j in zip(seq[::2], seq[1::2]):
        i = int(i)
        j = int(j)
        if swap:
            i, j = j, i
        result.append(grid[int(i)][int(j) - 1])
    return ''.join(result)


def encode(plaintext, key):
    return digits2symbols(symbols2digits(plaintext, key, True), make_grid(key))


def decode(plaintext, key):
    return encode(plaintext, key)

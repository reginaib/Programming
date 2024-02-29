# https://dodona.be/nl/courses/2802/series/29675/activities/413135075
"""
>>> normalize('Thank You Ash And Pikachu')
'THANKYOUASHANDPIKACHU'
>>> normalize('#ThankYouAshAndPikachu')
'THANKYOUASHANDPIKACHU'

>>> key = read_key('pokemon.txt4')
>>> key[25]
'PIKACHU'
>>> key[83]
'FARFETCHD'
>>> key[474]
'PORYGONZ'
>>> key[538]
'THROH'
>>> key[642]
'THUNDURUS'
>>> key[811]
'THWACKEY'
>>> key[828]
'THIEVUL'
>>> key[994]
'IRONMOTH'
>>> key[1111]
Traceback (most recent call last):
KeyError: 1111

>>> decode('#0828.2 #0979.2 #0382.3 #0197.1 #0460.1 #0319.3 #0932.1 #0927.1 #0025.7', key)
'THANKYOUASHANDPIKACHU'

>>> longest_common_prefix('THANKYOUASHANDPIKACHU', 'PIKACHU')
0
>>> longest_common_prefix('THANKYOUASHANDPIKACHU', 'THWAKEY')
2
>>> longest_common_prefix('ANKYOUASHANDPIKACHU', 'ANORITH')
2
>>> longest_common_prefix('KYOUASHANDPIKACHU', 'KYOGRE')
3

>>> longest_prefix('Thank You Ash And Pikachu', key)
({538, 642, 811, 828}, 2)
>>> longest_prefix('ANKYOUASHANDPIKACHU', key)
({347, 979}, 2)
>>> longest_prefix('KYOUASHANDPIKACHU', key)
({382}, 3)

>>> encode_prefix('Thank You Ash And Pikachu', key)
(828, 2)
>>> encode_prefix('ANKYOUASHANDPIKACHU', key)
(979, 2)
>>> encode_prefix('KYOUASHANDPIKACHU', key)
(382, 3)

>>> encode('Thank You Ash And Pikachu', key)
'#0828.2 #0979.2 #0382.3 #0197.1 #0460.1 #0319.3 #0932.1 #0927.1 #0025.7'
>>> encode('#ThankYouAshAndPikachu', key)
'#0828.2 #0979.2 #0382.3 #0197.1 #0460.1 #0319.3 #0932.1 #0927.1 #0025.7'
"""


def normalize(t):
    return ''.join(character for character in t.upper() if character.isalpha())


def read_key(location):
    with open(location, encoding='utf8') as file:
        return {int(k): normalize(v) for k, v in (line.split(maxsplit=1) for line in file)}


def decode(ciphertext, dictionary):
    result = []
    for code in ciphertext.split():
        idx, ln = code[1:].split('.')
        result.append(dictionary[int(idx)][:int(ln)])
    return ''.join(result)


def longest_common_prefix(string, key):
    n = 0
    for n, (c1, c2) in enumerate(zip(string, key)):
        if c1 != c2:
            return n
    return n + 1


def longest_prefix(t, d):
    ln = 0
    result = set()
    n = normalize(t)
    for k, v in d.items():
        x = longest_common_prefix(n, v)
        if x > ln:
            result = {k}
            ln = x
        elif x == ln:
            result.add(k)

    return result, ln


# def encode_prefix(prefix, key):
#     prefix_normalized = normalize(prefix)
#     min_id = float('inf')
#     max_length = 0
#
#     for key_id, key_name in key.items():
#         prefix_length = longest_common_prefix(prefix_normalized, key_name)
#         if prefix_length > max_length:
#             max_length = prefix_length
#             min_id = key_id
#         elif prefix_length == max_length:
#             min_id = min(min_id, key_id)
#
#     return min_id, max_length


def encode_prefix(plaintext, key):
    uids, length = longest_prefix(plaintext, key)
    assert length, 'encoding not possible'
    uid = min(uids, key=lambda uid: key[uid])
    return uid, length


# def encode(plaintext, key):
#     encoded_parts = []
#     while plaintext:
#         matching_ids, prefix_length = longest_prefix(plaintext, key)
#         min_id, _ = encode_prefix(plaintext[:prefix_length], key)
#         encoded_parts.append(f'#{str(min_id).zfill(4)}.{prefix_length}')
#         plaintext = plaintext[prefix_length:]
#     return ' '.join(encoded_parts)


def encode(plaintext, key):
    plaintext = normalize(plaintext)
    codes = []
    while plaintext:
        uid, length = encode_prefix(plaintext, key)
        codes.append(f'#{uid:04d}.{length}')
        plaintext = plaintext[length:]
    return ' '.join(codes)


if __name__ == '__main__':
    import doctest
    doctest.testmod()


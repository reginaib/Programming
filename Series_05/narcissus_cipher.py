def jump(alpha, n):
    assert isinstance(alpha, str), f'invalid letter: {alpha}'
    assert alpha.isalpha(), f'invalid letter: {alpha}'
    assert len(alpha) == 1, f'invalid letter: {alpha}'

    shift = ord('a') if alpha.islower() else ord('A')
    return chr(((ord(alpha) - shift + n) % 26) + shift)


def reflection(alpha, n):
    return jump(alpha, -n) + jump(alpha, n)


def fixation(pair, n):
    assert isinstance(pair, str), f'invalid pair: {pair}'
    assert len(pair) == 2, f'invalid pair: {pair}'
    assert pair.isalpha(), f'invalid pair: {pair}'
    assert pair.upper() == pair or pair.lower() == pair, f'invalid pair: {pair}'

    first_letter, second_letter = pair
    output = jump(first_letter, n)
    assert output == jump(second_letter, -n), f'invalid pair: {pair}'
    return output


def encode(plaintext):
    encoded_text = ''
    n = 1
    flag = False

    for char in plaintext:
        if char.isalpha():
            encoded_text += reflection(char, n)
            flag = True
        else:
            encoded_text += char
            if flag:
                n += 1
                flag = False
    return encoded_text


def decode(ciphertext):
    decoded_text = ''
    n = 1
    i = 0
    flag = False

    while i < len(ciphertext):
        char = ciphertext[i]
        if char.isalpha():
            pair = ciphertext[i:i+2]
            decoded_text += fixation(pair, n)
            i += 2
            flag = True
        else:
            decoded_text += char
            i += 1
            if flag:
                n += 1
                flag = False
    return decoded_text


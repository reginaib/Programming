def censored(word):
    return f'{word[0]}{len(word)}'


def revealed(word):
    output = ''
    digits = ''

    for char in word:
        if char.isdigit():
            digits += char
        else:
            if digits:
                output += '?' * (int(digits) - 1)
                digits = ''
            output += char
    if digits:
        output += '?' * (int(digits) - 1)
    return output


def censor(sentence):
    encoded_text = ''
    word = ''

    for char in sentence:
        if char.isalpha():
            word += char
        else:
            if word:
                encoded_text += censored(word)
                word = ''
            encoded_text += char
    if word:
        encoded_text += censored(word)

    return encoded_text


def reveal(censored_sentence):
    sentence = ''
    word = ''

    for char in censored_sentence:
        if char.isalpha() or char.isdigit():
            word += char
        else:
            if word:
                sentence += revealed(word)
                word = ''
            sentence += char
    if word:
        sentence += revealed(word)
    return sentence






def chemifyWord(word):
    i = 0
    for char in reversed(word):
        if char.lower() not in 'aeiouy':
            break
        i += 1
    if i:
        return word[:-i] + 'ium'
    elif word.endswith('ium'):
        return word
    return word + 'ium'


def chemify(sentence: str):
    output = ''
    word = ''
    for char in sentence:
        if char.isalpha():
            word += char
        else:
            if word:
                output += chemifyWord(word)
                word = ''
            output += char
    if word:
        output += chemifyWord(word)
    return output


    # return ' '.join(chemifyWord(word) for word in sentence.split())


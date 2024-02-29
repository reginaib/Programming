def salt(pile):
    return pile.count('#')


def gold(pile):
    out = 0
    for character in pile:
        if character.isdigit():
            out += int(character)
    return out


def remove_salt(pile):
    return pile.replace('#', '')


def remove_gold(pile):
    out = ''
    for char in pile:
        if char.isdigit():
            continue
        out += char
    return out


def trade(pile):
    s = salt(pile)
    g = gold(pile)

    if s > g:
        return remove_salt(pile)
    return remove_gold(pile)

def position(char):
    char = char.lower()
    return ord(char) - ord('a') + 1


def first_position(word):
    return min(position(char) for char in word)


def last_position(word):
    return max(position(char) for char in word)


def isfirst(word):
    # for letter in word:
    #     if position(letter) > 13:
    #         return False
    # return True

    return all(position(char) <= 13 for char in word)
    #return any(position(char) > 13 for char in word)


def issecond(word):
    # for letter in word:
    #     if position(letter) < 13:
    #         return False
    # return True

    return all(position(char) > 13 for char in word)


def isalternate(word):
    return not (isfirst(word) or issecond(word))

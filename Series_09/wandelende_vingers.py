# https://dodona.be/nl/courses/2802/series/29675/activities/574186898
from collections import defaultdict


def outside(word):
    return word[0] + word[-1]


def inside(word):
    return word[1:-1]


def issubword(word1, word2):
    word2_iter = iter(word2)

    previous = None
    for char1 in word1:
        if char1 == previous:
            continue
        previous = char1

        for char2 in word2_iter:
            if char1 == char2:
                break
        else:
            return False
    return True


def iswandering(word1, word2):
    return outside(word1) == outside(word2) and issubword(word1, word2)


def read_dictionary(file_name):
    result = defaultdict(set)
    with open(file_name, encoding='utf8') as file:
        for word in file:
            word = word.strip()
            result[outside(word)].add(inside(word))
    return dict(result)


def wanderings(word, dictionary):
    result = set()
    for ins in dictionary.get(outside(word), []):
        candidate = word[0] + ins + word[-1]
        if iswandering(candidate, word):
            result.add(candidate)
    return result

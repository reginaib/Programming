def side(letter, puzzle):
    for i, char in enumerate(puzzle):
        if letter in char:
            return i
    return -1


def iscomplete(solution, puzzle):
    for char in puzzle:
        if char not in solution:
            return False
    return True


def isconsecutive(solution):
    words = solution.split('-')

    for word1, word2 in range(len(words) - 1):
        if word1[-1] != word2[0]:
            return False
    return True


def iscrossing(solution, puzzle):
    for word in solution.split('-'):
        for char1, char2 in zip(word, word[1:]):
            if side(char1, puzzle) == side(char2, puzzle):
                return False
    return True

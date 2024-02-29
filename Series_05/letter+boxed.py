def side(letter, puzzle):
    # I am sure there is a shorter way to access the index of the list
    # and write is as print(idx) but now I go for the longer version because the lack of time
    if letter in puzzle.split('-')[0]:
        result = 0
    elif letter in puzzle.split('-')[1]:
        result = 1
    elif letter in puzzle.split('-')[2]:
        result = 2
    elif letter in puzzle.split('-')[3]:
        result = 3
    else:
        result = -1

    return result


def iscomplete(solution, puzzle):
    solution_letters = ''.join(solution.split('-'))
    puzzle_letters = ''.join(puzzle.split('-'))
    letter_count = [0] * 26

    #count = 0
    for char in solution_letters:
        if char in puzzle_letters:
            index = ord(char) - ord('A')
            letter_count[index] += 1
            #count += 1
    is_complete = all(count == 1 for count in letter_count)
    return is_complete


def isconsecutive(solution):
    first, second, third = solution.split('-')
    return first[-1] == second[0] or second[-1] == third[0]


def iscrossing(solution, puzzle):
    solution_letters = ''.join(solution.split('-'))
    i = 0
    flag = False
    while i < len(solution_letters):
        char = solution[i]
        char2 = solution[i+1]
        return side(char, puzzle) != side(char2, puzzle)


def issolution(solution, puzzle):
    return iscomplete(solution, puzzle) and isconsecutive(solution) and iscrossing(solution, puzzle)
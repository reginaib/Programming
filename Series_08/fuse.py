# https://dodona.be/nl/courses/2802/series/29674/activities/396622942
def list_representation(grid, n, m=None):
    """
    >>> grid = list_representation('1221133113322222', 4)
    >>> grid
    [[1, 2, 2, 1], [1, 3, 3, 1], [1, 3, 3, 2], [2, 2, 2, 2]]
    >>> list_representation('333333333333333', 3, 5)
    [[3, 3, 3, 3, 3], [3, 3, 3, 3, 3], [3, 3, 3, 3, 3]]
    """
    if m is None:
        m = n
    result = []
    row = []
    for char in grid:
        row.append(int(char))
        if len(row) == m:
            result.append(row)
            row = []
            if len(result) == n:
                return result


def string_representation(grid):
    """
    >>> grid =  [[1, 2, 2, 1], [1, 3, 3, 1], [1, 3, 3, 2], [2, 2, 2, 2]]
    >>> string_representation(grid)
    ('1221133113322222', 4, 4)
    """
    n = len(grid)
    m = len(grid[0])
    return ''.join(str(i) for row in grid for i in row), n, m


def move(num, pos, grid):
    """
    >>> grid = [[1, 2, 2, 1], [1, 3, 3, 1], [1, 3, 3, 2], [2, 2, 2, 2]]
    >>> move(-1, {(1, 2), (1, 1), (2, 1), (2, 2)}, grid)
    [[1, 2, 2, 1], [1, 2, 2, 1], [1, 2, 2, 2], [2, 2, 2, 2]]
    >>> grid =  [[1, 2, 2, 1], [1, 2, 2, 1], [1, 2, 2, 2], [2, 2, 2, 2]]
    >>> move(+1, {(0, 3), (1, 3)}, grid)
    [[1, 2, 2, 2], [1, 2, 2, 2], [1, 2, 2, 2], [2, 2, 2, 2]]
    >>> grid =  [[1, 2, 2, 2], [1, 2, 2, 2], [1, 2, 2, 2], [2, 2, 2, 2]]
    >>> move(+1, {(2, 0), (1, 0), (0, 0)}, grid)
    [[2, 2, 2, 2], [2, 2, 2, 2], [2, 2, 2, 2], [2, 2, 2, 2]]
    """
    for i, j in pos:
        grid[i][j] += num
    return grid


def is_solved(grid):
    """
    >>> grid =  [[2, 2, 2, 2], [2, 2, 2, 2], [2, 2, 2, 2], [2, 2, 2, 2]]
    >>> is_solved(grid)
    True
    >>> grid =  [[1, 2, 2, 2], [1, 2, 2, 2], [1, 2, 2, 2], [2, 2, 2, 2]]
    >>> is_solved(grid)
    False
    """
    return all(i == grid[0][0] for row in grid for i in row)


def group(position, grid):
    """
    >>> grid_01 = [[1, 2, 2, 1], [1, 3, 3, 1], [1, 3, 3, 2], [2, 2, 2, 2]]
    >>> group((2, 1), grid_01)
    {(1, 1), (1, 2), (2, 1), (2, 2)}
    >>> grid_02 = [[3, 3, 4, 5], [5, 4, 2, 3], [4, 2, 1, 1], [5, 5, 2, 4]]
    >>> group((0, 1), grid_02)
    {(0, 1), (0, 0)}
    """
    group, todo = set(), {position}
    rows, cols = len(grid), len(grid[0])
    number = grid[position[0]][position[1]]
    while todo:
        r, k = todo.pop()
        group.add((r, k))
        for dr, dk in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            if (
                    0 <= r + dr < rows
                    and 0 <= k + dk < cols
                    and (r + dr, k + dk) not in group
                    and grid[r + dr][k + dk] == number
            ):
                todo.add((r + dr, k + dk))
    return group


def is_solution(moves, grid):
    """
    >>> is_solution([(1, 1, False), (3, 2, False)], grid)
    True
    >>> is_solution([(1, 3, True), (3, 2, False), (0, 1, True)], grid)
    False
    """
    # deep copy of grid
    grid = [row[:] for row in grid]
    # perform moves
    for (row, col, increment) in moves:
        move(
            +1 if increment else -1,
            group((row, col), grid),
            grid
        )
    return is_solved(grid)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
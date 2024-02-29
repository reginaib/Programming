def even_odd(n):
    even = 0
    odd = 0
    while True:
        n, x = divmod(n, 10)
        if x % 2:
            odd += 1
        else:
            even += 1
        if not n:
            break
    return even, odd


def step(n):
    even, odd = even_odd(n)
    if even == 0:
        return int(str(odd) + str(odd))
    return int(str(even) + str(odd) + str(even + odd))


def steps(n):
    count = 0
    while n != 123:
        n = step(n)
        count += 1
    return count







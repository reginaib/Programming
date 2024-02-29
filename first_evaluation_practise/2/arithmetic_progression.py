def roll(num):
    return f'{num[-1]}{num[:-1]}'


def shift(num1, num2):
    result = ''

    for n1, n2 in zip(num1, num2):
        result += str((int(n1) + int(n2)) % 10)

    return result

def progression(num1, num2, num3):
    res = num1

    for _ in range(num3):
        res = shift(res, num2)

    for _ in range(num3):
        res = roll(res)

    return res


def period(num1, num2):
    count = 0
    while True:
        count += 1
        if num1 == progression(num1, num2, count):
            return count

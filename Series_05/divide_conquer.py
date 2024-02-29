def longest_polydivisible_prefix(num):
    num_str = str(num)
    prefix = ''
    for i in range(1, len(num_str) + 1):
        if int(num_str[:i]) % i != 0:
            return int(prefix)
        prefix = num_str[:i]
    return num


def ispolydivisible(num):
    return longest_polydivisible_prefix(num) == num


def polydivisible_extensions(num):
    count = 0
    for i in range(10):
        if ispolydivisible(num * 10 + i):
            count += 1
    return count
